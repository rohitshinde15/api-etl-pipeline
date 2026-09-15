import json
import requests
import time

new_list = []
pages = 0
total = None

try:
    while True:

        attempts = 0
        success = False

        while attempts < 3:

            response = requests.get(
                "https://dummyjson.com/users",
                params={
                    "limit": 100,
                    "skip": pages * 100
                },
                timeout=5
            )

            if response.status_code == 429:

                retry_after = response.headers.get("Retry-After")

                if retry_after:
                    wait_time = int(retry_after)
                else:
                    wait_time = 2

                attempts += 1

                print(
                    f"Rate limit exceeded. "
                    f"Waiting {wait_time} seconds... "
                    f"Retry attempt {attempts}/3"
                )

                time.sleep(wait_time)
                continue

            response.raise_for_status()

            data = response.json()

            # Get total number of users
            if total is None:
                total = data["total"]

            new_list.extend(data["users"])

            success = True
            break

        if not success:
            print(f"Failed to fetch page {pages + 1} after 3 attempts.")
            break

        print(f"Page {pages + 1} fetched successfully.")

        pages += 1

        # Stop when all users have been fetched
        if len(new_list) >= total:
            break

except requests.RequestException as e:
    print("Request failed:", e)


# ---------------- TRANSFORMATION ----------------

clean_list = []

for item in new_list:

    if item["age"] < 30:

        clean_user = {
            "id": item.get("id"),
            "First_Name": item.get("firstName"),
            "Last_name": item.get("lastName"),
            "Age": item.get("age"),
            "gender": item.get("gender", "unknown"),
            "email": item.get("email")
        }

        clean_list.append(clean_user)


# ---------------- SAVE RAW DATA ----------------

with open("raw.json", "w") as file:
    json.dump(new_list, file, indent=4)


# ---------------- SAVE CLEAN DATA ----------------

with open("clean_list.json", "w") as file:
    json.dump(clean_list, file, indent=4)


# ---------------- VALIDATION ----------------

ids = [item["id"] for item in new_list]

print()
print("Total available:", total)
print("Fetched records:", len(new_list))
print("Unique IDs:", len(set(ids)))
print("Clean records:", len(clean_list))
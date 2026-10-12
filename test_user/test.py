from models.users import Buyer

print("--- Validation Test ---")
print("Type 'exit' in ID to stop.\n")

while True:
    print("-" * 20)
    user_id = input("Enter ID: ")

    if user_id.lower() == 'exit':
        print("Test stopped.")
        break

    email = input("Enter Email: ")
    password = input("Enter Password: ")
    first_name = input("Enter First Name: ")

    try:
        buyer = Buyer(
            user_id=int(user_id),
            email=email,
            password=password,
            first_name=first_name

        )
        print(f"\n✅ Success! Buyer '{buyer.first_name}' created.")

    except ValueError as e:
        print(f"\n❌ Validation Error: {e}")

    except Exception:
        print("\n⚠️ Error: ID must be a number.")
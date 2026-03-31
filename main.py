from car import Car
from database import (initialize_database, import_cars, add_car, get_all_cars,
                      get_car_by_id, update_car, delete_car, search_cars)

def show_menu():
    print("\n" + "="*40)
    print("   🚗  CAR DEALERSHIP MANAGER")
    print("="*40)
    print("1. View all cars")
    print("2. Add a new car")
    print("3. Update a car")
    print("4. Delete a car")
    print("5. Search cars")
    print("6. Exit")
    print("="*40)
    return input("Enter your choice (1-6): ")


def add_car_flow():
    make = input("Enter care make:")    

    model = input("Enter cars model: ")
    print(f"Cars model, {model}")

    year = input("Enter cars year: ")
    print(f"Cars year is, {int(year)}")

    price = input("Enter cars price: ")
    print(f"Cars year is, {float(price):.2f}")

    mileage = input("Enter cars mileage: ")
    print(f"Cars mileage is, {int(mileage)}")

    car = Car(
      make=make,
      model=model,
      year=year,
      price=price,
      mileage=mileage
  )
    print(f"Car {model} is added")

    return add_car(car)



def view_all_cars_flow():
    cars = get_all_cars()

    if not cars:
        print ("There is no such car in inventory")
        return

    for car in cars:
        print (car)



def update_car_flow():
    car_id = int(input("Enter cars id: "))
    print(f"Car ID, {car_id}")

    car = get_car_by_id(car_id)

    if not car:
      print(f"No car found with ID {car_id}.")
      return

    print(f"Updating: {car}")
    print("Press Enter to keep the current value.\n")

    new_make = input(f"Make [{car.make}]: ")
    if new_make:
        car.make = new_make

    new_model = input(f"Model [{car.model}]: ")
    if new_model:
        car.model = new_model
    
    new_year = input(f"Year [{car.year}]: ")
    if new_year:
        car.year = int(new_year)

    new_price = input(f"Price [{car.price}] :")
    if new_price:
        car.price = float(new_price)

    new_mileage = input(f"Mileage [{car.mileage}] :")
    if new_mileage:
        car.mileage = int(new_mileage)

    print(f"\n Current details:\n{car}\n")
    return update_car(car)


def delete_car_flow():
    car_id = int(input("Enter cars id: "))
    print(f"Cars ID, {car_id}")

    car = get_car_by_id(car_id)

    if not car:
      print(f"No car found with ID {car_id}.")
      return

    print(f"Car to delete: {car}")

    confirm = input("Are you sure? (y/n)")
    if confirm != "y":
        print("The delete proces was cancelled")
        return
    
    delete = delete_car(car_id)
    if delete:
        print (f"Car {car_id} deleted seccesfully")
    else:
        print(f"Failed to delet car {car_id}")



def search_cars_flow():
    keyword = input("Enter search keyword: ").strip()

    results = search_cars(keyword)

    if not results:
        print("No matching cars found")
        return

    print(f"\n Found {len(results)} car(s):")
    for car in results:
        print(car)

        
    
def main():
    initialize_database()  # Always call this first!
    import_cars()          # Load sample data if the table is empty
    
    while True:
        choice = show_menu()
        
        if choice == "1":
            view_all_cars_flow()
        elif choice == "2":
            add_car_flow()
        elif choice == "3":
            update_car_flow()
        elif choice == "4":
            delete_car_flow()
        elif choice == "5":
            search_cars_flow()
        elif choice == "6":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter 1–6.")


if __name__ == "__main__":
    main()







    
    


  
    
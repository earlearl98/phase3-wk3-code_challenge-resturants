#!/usr/bin/env python3

from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Customer, Restaurant, Review

if __name__ == '__main__':
    fake = Faker()

    engine = create_engine('sqlite:///restaurants.sqlite')
    Session = sessionmaker(bind=engine)
    session = Session()


    session.query(Review).delete()
    session.query(Restaurant).delete()
    session.query(Customer).delete()
    session.commit()

    customers = []
    for _ in range(20):
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
        session.add(customer)
        customers.append(customer)

    restaurants = []
    for _ in range(10):
        restaurant = Restaurant(
            name=fake.company(),
            price=random.randint(1000, 20000)
        )
        session.add(restaurant)
        restaurants.append(restaurant)

    reviews = []
    for customer in customers:
        for restaurant in restaurants:
            star_rating = random.randint(1, 10)
            review = Review(
                star_rating=star_rating,
                customer=customer,
                restaurant=restaurant
            )
            session.add(review)
            reviews.append(review)

    session.commit()
    session.close()




















# from faker import Faker
# import random

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# from models import Customer, Restaurant, Review


# if __name__ == '__main__':
#     engine = create_engine('sqlite:///restaurants.sqlite')
#     Session = sessionmaker(bind=engine)
#     session = Session()

#     session.query(Customer).delete()
#     session.query(Restaurant).delete()
#     session.query(Review).delete()

#     fake = Faker()

#     customers = []
#     for i in range(20):
#       customer = Customer(
#         first_name =fake.first_name(), 
#         last_name= fake.last_name()
#         )

#     session.add(customer)
#     session = sessionmaker(bind=engine)
#     session = session()

#     session.query(Customer).delete()
#     session.query(Restaurant).delete()
#     session.commit()   
#     customers.append(customer)
    

#     restaurants = []
#     for i in range(10):
#       resturant = Restaurant(
#         name=fake.company(),
#         price=random.randint(1000,20000))

#       session.add(resturant)
#       session.commit()  
#       restaurants.append(resturant)


#     reviews = []
#     for customer in customers:
#       for restaurant in restaurants:
        
#         star_rating = random.randint(1, 5)
        
#         review = Review(
#             star_rating=random.SystemRandom().uniform(5, 10),
#             customer_id=customer.id,
#             restaurant_id=restaurant.id,
#         )
        
        
#         reviews.append(review)


#     session.add_all(reviews)
#     session.commit()
#     session.close()



    
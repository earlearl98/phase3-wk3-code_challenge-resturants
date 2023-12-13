from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    reviews = relationship('Review', back_populates='restaurant')

    def all_reviews(self, session):
        """Return a list of strings with all the reviews for this restaurant."""
        reviews = session.query(Review).filter_by(restaurant_id=self.id).all()
        return [review.full_review() for review in reviews]

    @classmethod
    def fanciest(cls, session):
        """Return the restaurant instance with the highest price."""
        return session.query(cls).order_by(cls.price.desc()).first()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    reviews = relationship('Review', back_populates='customer')

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        """Return the restaurant instance that has the highest star rating from this customer."""
        highest_rating_review = max(self.reviews, key=lambda review: review.star_rating, default=None)
        return highest_rating_review.restaurant if highest_rating_review else None

    def add_review(self, session, restaurant, rating):
        """Create a new review for the restaurant with the given `restaurant_id`."""
        review = Review(star_rating=rating, restaurant=restaurant, customer=self)
        session.add(review)
        session.commit()

    def delete_reviews(self, session, restaurant):
        """Remove all reviews for this restaurant."""
        session.query(Review).filter_by(restaurant=restaurant, customer=self).delete()
        session.commit()

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')

    def full_review(self):
        """Return a string formatted as follows: Review for {restaurant name} by {customer's full name}: {review star_rating} stars."""
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."


DATABASE_URL = "sqlite:///./restaurants.db"
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)


Session = sessionmaker(bind=engine)
session = Session()

























# from sqlalchemy import ForeignKey, Column, Integer, String, MetaData,Table
# from sqlalchemy.orm import relationship, backref
# from sqlalchemy.ext.declarative import declarative_base

# convention = {
#     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
# }
# metadata = MetaData(naming_convention=convention)

# Base = declarative_base(metadata=metadata)

# restaurant_customer=Table(
#   'restaurant_customers',
#     Base.metadata,
#     Column('restaurant_id', ForeignKey('restaurants.id'), primary_key=True),
#     Column('customer_id', ForeignKey('customers.id'), primary_key=True),
#     extend_existing=True,
# )

# class Restaurant(Base):
#     __tablename__ = 'restaurants'

#     id = Column(Integer(), primary_key=True)
#     name = Column(String())
#     price = Column(Integer)

#     reviews = relationship('Review', back_populates='restaurant')


#     customers= relationship('Customer', secondary=restaurant_customer, back_populates='restaurants')

#     def __repr__(self):
#       return  f'Restaurant(id={self.id}, ' + \
#               f' name={self. name}, ' + \
#               f'price={self.price})'


# class Customer(Base):
#     __tablename__ = 'customers'

#     id = Column(Integer(), primary_key=True)
#     first_name = Column(String())
#     last_name = Column(String())  

#     reviews = relationship('Review', back_populates='customer')


#     restaurants= relationship('Restaurant', secondary=restaurant_customer, back_populates='customers')


#     def __repr__(self):
#       return  f'Dev(id={self.id}, ' + \
#               f'first_name={self.first_name}' + \
#               f'last_name={self.last_name})' 



# class Review(Base):
#     __tablename__ = 'reviews'

#     id = Column(Integer(), primary_key=True)
#     restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
#     customer_id = Column(Integer(), ForeignKey('customers.id')) 
#     star_rating = Column(Integer())
    
#     # Add relationships
#     customer = relationship('Customer', back_populates='reviews')
#     restaurant = relationship('Restaurant', back_populates='reviews')

#     def __repr__(self):
#         return  f'Review(id={self.id}, ' + \
#                 f'restaurant_id={self.restaurant_id}'+ \
#                 f'star_rating={self.star_rating}'+ \
#                 f'customer_id={self.customer_id})' 
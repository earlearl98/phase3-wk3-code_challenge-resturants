# phase3-wk3-code_challenge-resturants


# Restaurant Review Management System
This project is a Restaurant Review Management System built using SQLAlchemy and Flask. The system allows users to manage restaurants, customers, and reviews, and provides various methods for retrieving, aggregating, and interacting with the data.

# Table of Contents

- Installation
- Usage
- Database Setup
- Object Relationship Methods
- Aggregate and Relationship Methods
- Contributing
- License

# Installation

1.Clone the Repository
2.Install Dependencies

# Usage
This system provides a set of methods for managing restaurants, customers, and reviews.

# Database Setup
Ensure that you have a database named restaurants.sqlite configured for this system. The database will be created automatically during the migration process.

# Object Relationship Methods
# Review Class
Review customer(): Returns the Customer instance for this review.
Review restaurant(): Returns the Restaurant instance for this review.

# Restaurant Class
Restaurant reviews(): Returns a collection of all the reviews for the Restaurant.
Restaurant customers(): Returns a collection of all the customers who reviewed the Restaurant.

# Customer Class
Customer reviews(): Returns a collection of all the reviews that the Customer has left.
Customer restaurants(): Returns a collection of all the restaurants that the Customer has reviewed.

Ensure that these methods work by querying the database for sample data.

# Aggregate and Relationship Methods

# Customer Class

Customer full_name(): Returns the full name of the customer, with the first name and the last name concatenated, Western style.
Customer favorite_restaurant(): Returns the restaurant instance that has the highest star rating from this customer.
Customer add_review(restaurant, rating): Creates a new review for the restaurant with the given restaurant_id.
Customer delete_reviews(restaurant): Removes all reviews for the specified restaurant.
# Review Class

Review full_review(): Returns a string formatted as follows: "Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars."
# Restaurant Class
Restaurant fanciest() (class method): Returns one restaurant instance for the restaurant that has the highest price.
Restaurant all_reviews(): Returns a list of strings with all the reviews for this restaurant, formatted as specified.

Ensure that these methods work as expected by testing them with the provided sample data.

# Contributing
If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: git      checkout -b feature-name.
3. Commit your changes: git commit -m 'Add some feature'.
4. Push to the branch: git push origin feature-name.
5. Submit a pull request.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
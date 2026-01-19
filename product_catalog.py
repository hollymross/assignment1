from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.

#print(products)

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.

customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list

    customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.



# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []

for product in products:
    converted_product = product.copy()
    converted_product["tags"] = set(product["tags"])
    converted_products.append(converted_product)


# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags.intersection(customer_tags))




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    rec_products = []

    for product in products:
        match_count = count_matches(product["tags"], customer_tags)
        rec_products.append({"name": product["name"],"matches": match_count})

    return rec_products

# TODO: Step 7 - Call your function and print the results

results = recommend_products(converted_products, customer_preferences)

for x in results:
    print(x['name'] + " - Matches: " + str(x['matches']))


# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
#Some of the operations I used included intersection, append, and loops. The loops were used to go through all the product data and find matches in the tags that the customer added as 
#preferences. I also used a loop for my print statement to go through all the products and show how many matches in the tags that there were for the customer to be able to view. I used
#intersections and view the tags in both the product data and the customer preferences to find matches. Lastly I used append to add things into the lists and the converted those lists
#into sets to reduce repetition.
# 2. How might this code change if you had 1000+ products?
#If there were 1000+ products there are a couple things that would change. First it would be best to not convert all the data from a list to a set every time we run the code because
#it could increase the runtime and it would be redundant. Rather we could do this in the product data code so it is already non repetative and ready to be used. We could also have the
#print statment only return the top few matches for the customer to view, or they could select how many product matches they want to be able to view. 

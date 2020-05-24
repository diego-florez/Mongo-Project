# Mongo-Project -- Find Your Startup Location

#3 1.Intro:
In this repository you will find a project about geolocation. In this case, we will try to find the perfect location for a startup based in some conditions.

## 2.Goals:
The main goal of this project is to find the perfect location for a startup based in some conditions. Also, the second goal is to create map with the final coordinates of the location.

## 3.Steps:
To fulfil the previous goals the next steps have been done:

src (acquire data through api request and compute all the backstage)
main.ipynb (the start, knot and outcome of the project, without the backstage functions)
OUTPUT (where dataframes and map are)

## 4.Final Output:
The final output is a map with the "perfect" location for an startup based in some conditions.

### Additional Info:
1. Source: Crunchbase companies data
2. Conditions:
- 30% of the company have at least 1 child.
- Developers like to be near successful tech startups that have raised at least 1 Million dollars.
- Executives like Starbucks A LOT. Ensure there's a starbucks not to far.
- Account managers need to travel a lot
- All people in the company have between 25 and 40 years, give them some place to go to party.
- Nobody in the company likes to have companies with more than 10 years in a radius of 2 KM.
- The CEO is Vegan

# Process:
1. We start from a dataset of companies from Crunchbase (year 2013).
2. We import it to mongoDB and then load it in jupyter.
3. In jupyter main, we extract, in 3 steps, the tech startups, with more than 1M raised, out of a radius of 2km of old companies. (remember the source is from 2013).
4. After we have a small dataframe with 9 possible opts, we choose one of the opts based in the conditions we consider more important.
5. We look for the coordinates of the conditions (places) of the selected opt, requesting Google API Places.
6. Finally we load it in an interactive map.

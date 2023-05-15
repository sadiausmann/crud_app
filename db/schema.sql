CREATE DATABASE recipe_app;

\c recipe_app

CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  email TEXT,
  password_digest TEXT
);

CREATE TABLE recipes(
  id SERIAL PRIMARY KEY,
  user_id INTEGER,
  title TEXT,
  image_url TEXT,
  ingredients TEXT,
  recipe TEXT
);

CREATE TABLE comments(
  id SERIAL PRIMARY KEY,
  recipe_id INTEGER,
  user_id INTEGER,
  comment TEXT NOT NULL
);

CREATE TABLE likes(
  id SERIAL PRIMARY KEY,
  user_id INTEGER,
  recipe_id INTEGER
);

INSERT INTO recipes(user_id, title, image_url, ingredients, recipe)
VALUES
(0,'Chicken Pasta','https://images.unsplash.com/photo-1530334044505-5b3aa24cb147?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8Y2hpY2tlbiUyMHBhc3RhfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60',
'2 chicken breasts cut in strips
1 tablespoon olive oil
1/2 medium yellow onion chopped
1/2 bell pepper chopped
3 cloves of garlic minced
1/2 teaspoon EACH salt, pepper, & garlic powder
1 cup marinara sauce
1/2 cup mozzarella or Italian blend cheese
1/4 cup Parmesan cheese optional
3 cups cooked pasta 1.5 cups dry pasta',
'In a medium saucepan, bring 2 cups of salted water to boil, pour 1.5 cups of uncooked pasta and 1 tsp salt into the water. Cover and allow to cook for 10 minutes.
While the pasta is cooking, cut chicken breasts and, onion and bell peppers. Heat 1 tablespoon oil in a heavy-duty pan or pot over medium-high heat. Add the onion and bell pepper and saute for 1-2 minutes or until softened. Add the garlic and sautee 30 seconds or until lightly golden. Add the chicken, salt, pepper, & garlic powder and saute until the chicken is browned and almost cooked through.
Add the marinara sauce and allow to simmer for 5 minutes while the pan is covered. After 5 minutes, drain the water from the pasta and pour pasta on the chicken mixture. Mix well, add the cheese and turn off. The cheese will melt from the heat of the pan. If desired, broil the cheese under the broiler in the oven until bubbly.
Top with Parmesan and enjoy!'),
(0,'Chicken lettuce wraps', 'https://images.unsplash.com/photo-1512852939750-1305098529bf?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OXx8Y2hpY2tlbiUyMGluJTIwbGV0dHVjZXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60', 
'2-3 chicken breasts medium size, diced
1 tbsp olive oil light
3 garlic cloves minced
1 tsp ginger fresh and grated
2 green onions sliced with the whites & greens separated
¼ cup red bell peppers diced
lettuce leaves iceberg or butter lettuce',
'Start by mixing all the sauce ingredients together in a small bowl and set aside.
Heat the olive oil in a pan over medium heat. Add the ginger, garlic, and white parts of the green onions. Cook the mixture until you can start to smell it, which will take about 1 minute.
Add the chicken to the mixture and cook for 4-5 minutes. The chicken should be almost cooked all the way, but not quite. Add the bell pepper and sauce. Cook the mixture for 3-4 minutes, until the sauce is thick and the chicken is fully cooked.
Serve by adding 1/4 cup of the mixture into a lettuce leaf.'),
(0,'Chocolate Chip MUffins','https://plus.unsplash.com/premium_photo-1669452304930-6b3e7d33c596?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8N3x8Y2hvY29sYXRlJTIwY2hpcCUyMG11ZmZpbnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60' ,
'1 1/2 cups all-purpose flour 
2 tsp baking powder
1/2 tsp salt
1/2 cup unsalted butter, melted
1 cup granulated sugar
1/4 cup sour cream, at room temperature
2 eggs at room temperature
1/2 cup milk
1 tbsp 
1 cup mini chocolate chips',
'Preheat the oven to 375 degree F. Line the muffin pan with cupcake liners and keep it aside.
In a medium bowl combine the dry ingredients together; flour, baking powder, baking soda, and salt.
In a large bowl combine the wet ingredients; whisk the melted butter and sugar.  
Crack the eggs and combine with the wet ingredients. Add in the vanilla, sour cream, and milk.
Gently fold in the dry ingredients to the wet ingredients.
In a small bowl with a teaspoon of flour coat the chocolate chips and toss it. Fold the chocolate chips into the batter. 
With the help of an ice cream scooper; scoop the batter equally into 12 muffin liners. Bake in the preheated oven for 20 to 25 minutes, until a toothpick inserted into the center comes out clean.
Place the muffins on a wire rack and serve them once cool down.'),
(0,'Avacado Chicken Salad','https://images.unsplash.com/photo-1505253716362-afaea1d3d1af?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8Y2hpY2tlbiUyMGluJTIwbGV0dHVjZXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60',
'2 medium cooked chicken breasts shredded or chopped (we used rotisserie chicken)
2 ripe avocados pitted and diced
1/2 cup corn roasted, canned, or frozen
1/4 cup red or green onion minced
2 tablespoons cilantro minced (or parsley or dill)
2 tablespoons lime or lemon juice
2 tablespoons olive oil
salt and pepper to taste',
'In a large bowl, add the shredded chicken, avocado, onion, avocados, corn, and cilantro.
Drizzle with the lime (or lemon) juice, olive oil and season with salt and pepper. Toss gently until all the Ingredients are combined.'),
(0,'Chicken wraps','https://images.unsplash.com/photo-1626700051175-6818013e1d4f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Y2hpY2tlbiUyMHdyYXB8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60',
'4 MorningStar Farms Chick Patties
4 large 8-10'' flour tortillas
1 medium tomato sliced
1 small onion sliced
4 leafs Romain lettuce
2 teaspoons buffalo sauce
2 teaspoons ranch dressing
1 teaspoon oil if toasting',
'Heat Patties according to package directions. Cut into thin slices and set aside.
Arrange flour tortilla flat on a plate. Add Romain lettuce (omit if toasting), then onions and tomatoes. Top with chicken, drizzle 1/2 teaspoon buffalo sauce and 1/2 teaspoon ranch dressing; wrap tightly. repeat processor for remaining tortillas. After this step you can choose to eat the sandwich like this without toasting or continue to step two for the crispy version.
Heat a large skillet to medium/high heat, add teaspoon oil. Place tortilla seam down on the pan. cook for 1 minute on each side or until golden in color. Remove from heat. Serve warm Enjoy!'),
(0,'Chicken Fried Rice','https://plus.unsplash.com/premium_photo-1668782623937-56d6d64a7f36?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8Y2hpY2tlbiUyMGZyaWVkJTIwcmljZXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60',
'1/2 pound boneless skinless chicken breasts diced into 1/2 inch pieces
2 tablespoons oil peanut, sesame, vegetable, or canola
1/2 cup white onion finely chopped
1 cup frozen peas and dice carrots blend
2 cloves garlic finely minced
2 large eggs lightly beaten
3 cups white long grain rice cooked
3-4 tablespoons low-sodium soy sauce
salt to taste
pepper optional, to taste
1-2 tablespoons  optional, to taste',
'Heat a large non-stick wok or skillet to medium-high heat. Add the cut chicken and oils; sautee for 4-5 minutes. Remove chicken from the skillet and add the carrots, peas, and onions to the same skillet. Sautee another 2-3 minutes then add the garlic and cook another minute. 
Push the veggies to one side of the skillet and add the eggs to the other side and scramble.
Return chicken to the skillet along with the rice and soy sauce. Stir-fry another 2-3 minutes.
Taste and adjust seasoning if needed. We like to add 1-2 tablespoons sriracha to add a spicy kick. Serve hot; Garnish with green onion if desired.
To store: In an airtight container for up to 4 days or freezer for up to 4 months.')
 
from db.db import sql

def all_recipes():
    return sql("SELECT * FROM recipes ORDER by id")

def create_recipe(user_id,title,image_url,ingredients,recipe):
    sql('INSERT INTO recipes(user_id,title,image_url,ingredients,recipe) VALUES(%s, %s, %s, %s, %s) RETURNING *',[user_id,title,image_url,ingredients,recipe])

def get_recipe(id):
    recipes = sql("SELECT * FROM recipes WHERE id = %s",[id])
    return recipes[0]

def update_recipe(user_id ,title, image_url,  ingredients, recipe, id):
    sql("UPDATE recipes SET user_id=%s, title=%s, image_url=%s, ingredients=%s, recipe=%s WHERE id=%s RETURNING *",[user_id, title, image_url, ingredients, recipe, id])

def delete_recipe(id):
    sql("DELETE FROM recipes WHERE id=%s RETURNING *",[id])

def like_recipe(recipe_id, user_id):
    check_if_already_liked = sql('SELECT * FROM likes WHERE user_id = %s AND recipe_id = %s', [user_id, recipe_id])
    if len(check_if_already_liked)>0:
        sql('DELETE FROM likes WHERE user_id=%s AND recipe_id=%s RETURNING *',[user_id, recipe_id])
    else:
        sql("INSERT INTO likes(user_id, recipe_id) VALUES(%s, %s) RETURNING *", [user_id, recipe_id])

def comment_recipe(recipe_id, user_id, comment):
    sql("INSERT INTO comments (recipe_id, user_id, comment) VALUES (%s, %s, %s) RETURNING *",[recipe_id, user_id, comment])

def all_comments(recipe_id):
    return sql("SELECT * FROM comments WHERE recipe_id =%s",[recipe_id])

def all_likes(recipe_id):
    return sql('SELECT COUNT(*) FROM likes WHERE recipe_id = %s', [recipe_id])




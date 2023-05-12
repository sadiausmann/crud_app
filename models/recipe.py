from db.db import sql

def all_recipes():
    return sql("SELECT * FROM recipes ORDER by id")

def create_recipe(user_id,title,image_url,ingredients,recipe):
    sql('INSERT INTO recipes(user_id,title,image_url,ingredients,recipe) VALUES(%s, %s, %s, %s, %s) RETURNING *',[user_id,title,image_url,ingredients,recipe])

def get_recipe(id):
    recipes = sql("SELECT * FROM recipes WHERE id = %s",[id])
    return recipes[0]

def update_recipe(title, image_url,  ingredients, recipe, id):
    sql('UPDATE recipes SET title=%s, image_url=%s WHERE id=%s RETURNING *',[title, image_url, ingredients, recipe, id])

def delete_recipe(id):
    sql('DELETE FROM recipes WHERE id=%s RETURNING *',[id])
from lib.recipes import Recipes

class Recipes_Repository:
    def __init__(self, connection):
        self._connection = connection
        
    def all(self):
        rows = self._connection.execute('SELECT * from recipes')
        recipes = []
        for row in rows:
            item = Recipes(row["id"], row["recipe_name"], row["cooking_time"], row["rating"])
            recipes.append(item)
        return recipes 
    
    def find(self, recipe_name):
        rows = self._connection.execute(
            'SELECT * from recipes WHERE id = %s', [recipe_name])
        row = rows[0]
        return Recipes(row["id"], row["recipe_name"], row["cooking_time"], row["rating"])
        
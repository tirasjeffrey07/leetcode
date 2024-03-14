class FoodRatings:
    foodSystem = {}
    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        for i in range(len(foods)):
            FoodRatings.foodSystem.__setitem__(cuisines[i],[ratings[i],foods[i]])
        
    def changeRating(self, food: str, newRating: int) -> None:
        # iterating through only the food items of the values of the dictionary
        for foodItem in FoodRatings.foodSystem.values()[1]:
            if foodItem == food:
                FoodRatings.foodSystem.values()[0] = newRating


    def highestRated(self, cuisine: str) -> str:
        temp = sorted(FoodRatings.foodSystem.items(),key=lambda x:x[1][0],reverse=True)
        for food in temp:
            if food[1][0] == cuisine:
                return food[0]

obj1 = FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7])
        
print(obj1.highestRated("korean"))

print(list(FoodRatings.foodSystem.values())[1])
# sorting the dictionary based on second value in the list (which is the value) of the key 
# thats why we use lambda x:x[1][1] 
print(sorted(FoodRatings.foodSystem.items(),key=lambda x:x[1][1],reverse=True))
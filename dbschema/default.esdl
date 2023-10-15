module default {
    type Recipe {
        required name: str,
        description: str,
        multi ingredients: Ingredient,
        instructions: array<str>,
        cuisine: str,
        category: str,
        price: float32,
        servings: int32,
        cooking_time;
    }

    type Ingredient {
        required name: str,
        isEssential: bool {
            default := False;
        },
        last_bought: cal::local_date,
        shelf_life: int32 {
            default := 7;
        };
    }
}

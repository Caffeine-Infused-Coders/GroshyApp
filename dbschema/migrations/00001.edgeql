CREATE MIGRATION m1lydtzjfc36fglbycrxyyg4voer6xu3dhvgyx74cj77i46tapnfaq
    ONTO initial
{
  CREATE TYPE default::Ingredient {
      CREATE PROPERTY isEssential: std::bool {
          SET default := false;
      };
      CREATE PROPERTY last_bought: cal::local_date;
      CREATE REQUIRED PROPERTY name: std::str;
      CREATE PROPERTY shelf_life: std::int32 {
          SET default := 7;
      };
  };
  CREATE TYPE default::Recipe {
      CREATE MULTI LINK ingredients: default::Ingredient;
      CREATE PROPERTY category: std::str;
      CREATE PROPERTY cooking_time: std::duration;
      CREATE PROPERTY cuisine: std::str;
      CREATE PROPERTY description: std::str;
      CREATE PROPERTY instructions: array<std::str>;
      CREATE REQUIRED PROPERTY name: std::str;
      CREATE PROPERTY price: std::float32;
      CREATE PROPERTY servings: std::int32;
  };
};

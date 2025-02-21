from textwrap import dedent

from groshy.recipe import Recipe


def _ask_field(field: str, update: bool, pmsg: str = "") -> str:
    resp = "None"

    if pmsg:
        msg = pmsg
    elif update and not pmsg:
        msg = f"Please provide a new {field} for the recipe: "
    else:
        msg = f"Recipe {field}: "

    resp = input(msg)

    return resp


"TODO: Allow method to accept a file path. Recipe should be built by reading said file"


def write_recipe(fp: str = "None") -> Recipe:
    """Prompts the user to provide information for the recipe fields before
    creating a Recipe object

        :param - fp: Path to text file containing recipe. Defaults to 'None'"""

    recipe = Recipe.make_empty_recipe()  # Return value defined here

    def get_list(field: str, msg: str):

        instructs = False
        anotherone = True
        stepnum = 0
        lst = []

        print(
            f"""{msg}

                Enter 'done' when all {field} have been accounted for\n"""
        )

        if "instructions" in msg:
            instructs = True

            def inc_msg(num):
                num += 1
                return num, f"Step {num}: "

        else:
            msg = "- "

        while anotherone:

            if instructs:
                stepnum, msg = inc_msg(stepnum)

            t = input(msg)

            if t == "done":
                anotherone = False

            else:
                lst.append(t)

        if not instructs:
            lst = Recipe.gather_ingredients(lst)

        return lst

    def print_list(type, lst):
        print(f"{type}: ")

        for idx, t in enumerate(lst, start=1):
            print(f"{idx}. {t}")
            if idx == len(lst):
                print("\n")

    recd = {
        "name": " ",
        "description": " ",
        "ingredients": [],
        "instructions": [],
        "category": " ",
        "cuisine": " ",
        "yields": " ",
        "cooking_time": 0,
    }

    recd["name"] = _ask_field("name", False, "What's the name of your recipe? ")

    recd["description"] = _ask_field(
        "description",
        False,
        "Please provide a \
short description for your recipe: \n",
    )

    recd["ingredients"] = get_list(
        "ingredients",
        dedent(
            """
Next we will create your list of ingredients. Please enter your ingredients \
in the following format:            
\n\t{amount} {unit} of {ingredient}
\n\ti.e. 1/3 cup of sugar.\n

Where it is important to add notes please do so in parentheses \
i.e 1 Tbsp Butter (softened))"""
        ),
    )

    recd["instructions"] = get_list(
        "instructions",
        dedent(
            """
The recipe instructions will be 
saved as a list of steps similar to how \
they are portrayed in a cookbook.
Please submit them this way \
by pressing the enter key when done writing each step."""
        ),
    )

    recd["category"] = _ask_field(
        "category",
        False,
        "What category of food \
is this recipe?: ",
    )

    recd["cuisine"] = _ask_field(
        "cuisine",
        False,
        "What type of cuisine \
is this recipe?: ",
    )

    recd["yields"] = _ask_field(
        "yields",
        False,
        "How many servings \
does this recipe yield?: ",
    )

    recd["cooking_time"] = int(
        _ask_field(
            "cooking_time",
            False,
            """How long 
does the recipe take to make in minutes
(total time)?: """,
        )
    )

    print(
        f"""Does this information look correct?:
                title: {recd["name"]}
                description: {recd["description"]}
                category: {recd["category"]}
                cuisine: {recd["cuisine"]}
                yields: {recd["yields"]}
                cooking time: {recd["cooking_time"]}"""
    )
    print_list("ingredients", recd["ingredients"])
    print_list("instructions", recd["instructions"])

    resp = input("Correct? (y/n): ")

    match resp.lower():
        case "y" | "yes":
            recipe = Recipe(**recd)
        case "n" | "no":
            wrong = input("Which entry is wrong?: ")

            try:
                recd[wrong] = _ask_field(wrong, True)
                recipe = Recipe(**recd)
            except KeyError as err:
                print(
                    f"{err}: Ha nice one... that's not what I was asking \
                          I'm returning an empty Recipe just fyi"
                )

    return recipe

# =====================================================
# MENU GROUP
# =====================================================

menu_group = {
    "roti": [
        "bagel", "salt_bread", "toast", "croissant",
        "danish", "sandoichi", "bungeoppang"
    ],

    "kue": [
        "cake", "lava_cake", "chiffon", "swiss_roll",
        "bolu", "mille_crepes", "scone"
    ],

    "roti_krispi": [
        "choux", "eclair", "puff",
        "macaroon", "cookies", "ganache"
    ],

    "es": [
        "ice_cream", "gelato", "sorbet",
        "es_serut", "sundae"
    ],

    "gorengan": [
        "donut", "waffle"
    ],

    "dessert_lembut": [
        "pudding", "mousse", "tiramisu",
        "mochi", "yogurt", "cheesecake",
        "tart", "pie", "dessert_box"
    ],

    "middle_east": [
        "kunafa"
    ],

    "lainnya": [
        "gamchi", "gabin"
    ],
}

# =====================================================
# FLAVOR GROUP
# =====================================================

flavor_group = {

    "chocolate": [
        "chocolate",
        "dark_chocolate",
        "white_chocolate",
        "dubai_chocolate",
        "chocolate_crunchy",
        "chocolate_nebula",
        "nutella",
        "ferrero",
        "dirty_milo",
        "chocolate_mint",
        "hazelnut",
        "pisang_chocolate"
    ],

    "fruity": [
        "fruity",
        "strawberry",
        "strawberry_cream",
        "milky_strawberry",
        "raspberry",
        "raspberry_shortcake",
        "blueberry",
        "mango",
        "melon",
        "banana",
        "banana_crunch",
        "coconut",
        "lemon",
        "peach",
        "peach_earl_grey",
        "lychee",
        "apple",
        "carrot",
        "berry",
        "srikaya",
        "mix_fruit",
        "durian",
        "taro",
        "ube",
        "pandan",
        "pumpkin",
        "yakult",
        "yuzu"
    ],

    "matcha": [
        "matcha",
        "matcha_crunch"
    ],

    "cheesy": [
        "cheese",
        "milk_cheese",
        "vanilla_cheese"
    ],

    "caramel": [
        "caramel",
        "salted_caramel",
        "salted",
        "brulee",
        "mochizu_brulee"
    ],

    "vanilla": [
        "vanilla",
        "blue_vanilla"
    ],

    "cookies": [
        "oreo",
        "cookies_cream",
        "cookie_monster",
        "lotus_biscoff",
        "cereal"
    ],

    "nutty": [
        "pistachio",
        "dubai_pistachio",
        "almond",
        "peanut",
        "sesame",
        "black_sesame",
        "red_bean",
        "roasted_rice"
    ],

    "floral_spice": [
        "jasmine",
        "jasmine_bergamot",
        "chamomile",
        "rose_oolong",
        "earl_grey",
        "cinnamon",
        "honey"
    ],

    "classic": [
        "original",
        "milk",
        "cream",
        "butter",
        "black_forest",
        "red_velvet",
        "shortcake",
        "sea_salt",
        "grass_jelly",
        "tiramisu"
    ]
}

# =====================================================
# HELPER FUNCTIONS
# =====================================================

def get_menu_group(menu_kw):
    menu_kw = menu_kw.lower()

    for group, members in menu_group.items():
        if menu_kw in members:
            return group

    return None


def get_flavor_group(flavor_kw):
    flavor_kw = flavor_kw.lower()

    for group, members in flavor_group.items():
        if flavor_kw in members:
            return group

    return None
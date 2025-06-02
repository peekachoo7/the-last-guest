class ActionKind(Enum):
    Walking = 0
    Idle = 1
    Jumping = 2

def on_up_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . . . . . . . . . . .
                . . . . . . f f f f f f f f . . .
                . . . . f f 8 8 8 8 8 8 8 8 f . .
                . . . f 8 8 8 8 8 6 8 8 8 8 8 f .
                . . f f 8 6 6 6 6 6 8 8 8 8 f . .
                . . f 6 6 6 8 8 8 8 8 8 8 f . . .
                . . f 6 8 8 8 8 8 8 8 6 6 f . . .
                . . f 8 8 8 8 6 6 6 6 8 8 f . . .
                . . f 8 8 8 6 6 8 8 8 8 8 f . . .
                . . f 8 8 6 6 8 8 8 8 8 8 f . . .
                . . f 1 1 8 8 8 8 8 8 1 1 f . . .
                . . . f 1 1 1 1 1 1 1 1 f . . . .
                . . 7 e f f f f f f f f e 7 . . .
                . . e 7 f e 7 7 7 e e f 7 e . . .
                . . 1 1 f 7 7 7 7 7 e f 1 1 . . .
                . . . . . e e 7 e 7 7 . . . . . .
                . . . . . e e . . e e . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . . .
                . . . . . . f f f f f f f f . . .
                . . . . f f 8 8 8 8 8 8 8 8 f . .
                . . . f 8 8 8 8 8 6 8 8 8 8 8 f .
                . . f f 8 6 6 6 6 6 8 8 8 8 f . .
                . . f 6 6 6 8 8 8 8 8 8 8 f . . .
                . . f 6 8 8 8 8 8 8 8 6 6 f . . .
                . . f 8 8 8 8 6 6 6 6 8 8 f . . .
                . . f 8 8 8 6 6 8 8 8 8 8 f . . .
                . . f 8 8 6 6 8 8 8 8 8 8 f . . .
                . . f 1 1 8 8 8 8 8 8 1 1 f . . .
                . . . f 1 1 1 1 1 1 1 1 f . . . .
                . . . e f f f f f f f f 1 1 . . .
                . . . 7 f 7 7 7 7 7 e e 7 1 . . .
                . . . 1 f e e 7 7 f 7 7 e . . . .
                . . . . f e e . . . . . . . . . .
                . . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . . .
                . . . . . . f f f f f f f f . . .
                . . . . f f 8 8 8 8 8 8 8 8 f . .
                . . . f 8 8 8 8 8 6 8 8 8 8 8 f .
                . . f f 8 6 6 6 6 6 8 8 8 8 f . .
                . . f 6 6 6 8 8 8 8 8 8 8 f . . .
                . . f 6 8 8 8 8 8 8 8 6 6 f . . .
                . . f 8 8 8 8 6 6 6 6 8 8 f . . .
                . . f 8 8 8 6 6 8 8 8 8 8 f . . .
                . . f 8 8 6 6 8 8 8 8 8 8 f . . .
                . . f 1 1 8 8 8 8 8 8 1 1 f . . .
                . . . f 1 1 1 1 1 1 1 1 f . . . .
                . . 7 e f f f f f f f f e 7 . . .
                . . e 7 f e 7 7 7 e e f 7 e . . .
                . . 1 1 f 7 7 7 7 7 e f 1 1 . . .
                . . . . . e e 7 e 7 7 . . . . . .
                . . . . . e e . . e e . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . . .
                . . . . . . f f f f f f f f . . .
                . . . . f f 8 8 8 8 8 8 8 8 f . .
                . . . f 8 8 8 8 8 6 8 8 8 8 8 f .
                . . f f 8 6 6 6 6 6 8 8 8 8 f . .
                . . f 6 6 6 8 8 8 8 8 8 8 f . . .
                . . f 6 8 8 8 8 8 8 8 6 6 f . . .
                . . f 8 8 8 8 6 6 6 6 8 8 f . . .
                . . f 8 8 8 6 6 8 8 8 8 8 f . . .
                . . f 8 8 6 6 8 8 8 8 8 8 f . . .
                . . f 1 1 8 8 8 8 8 8 1 1 f . . .
                . . . f 1 1 1 1 1 1 1 1 f . . . .
                . . 1 1 f f f f f f f f e . . . .
                . . 1 7 e e 7 e 7 e e f 7 . . . .
                . . . e 7 7 f 7 7 7 7 f 1 . . . .
                . . . . . . . . . e e f . . . . .
                . . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_on_score():
    game.set_game_over_message(True, "Bacons have been defeated")
    game.game_over(True)
info.on_score(250, on_on_score)

def on_button_released():
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
controller.any_button.on_event(ControllerButtonEvent.RELEASED, on_button_released)

def on_left_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . f f f f f f f . . . . . .
                . . f f 8 8 6 6 8 8 f f . . . .
                . . f 8 6 6 8 6 6 8 8 f f . . .
                . . f 8 8 6 6 8 6 8 8 8 f . . .
                . . f 8 8 8 6 8 6 6 8 8 f . . .
                . . f 8 8 8 6 8 8 6 8 8 f . . .
                . . f 1 1 1 1 8 8 8 8 8 f . . .
                . . f 1 1 1 f 1 1 1 8 8 f . . .
                . . f 1 1 1 f 1 1 1 1 8 f . . .
                . . . f 1 1 1 1 1 1 1 1 f . . .
                . . . f 7 7 7 7 e e f f . . . .
                . . . f 7 e e 7 e 7 f . . . . .
                . . . f 7 e e 7 7 e f . . . . .
                . . . f e 7 7 f 1 1 f . . . . .
                . . . . f f e 7 f f . . . . . .
                . . . . . . e 7 e . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . f f f f f f . . . . . .
                . . . f 8 8 6 6 8 8 f f . . . .
                . . f 8 6 6 8 6 6 8 8 f f . . .
                . . f 8 8 6 6 8 6 8 8 8 f . . .
                . . f 8 8 8 6 8 6 6 8 8 f . . .
                . . f 8 8 8 6 8 8 6 8 8 f . . .
                . . f 1 1 1 1 8 8 8 8 8 f . . .
                . . f 1 1 1 f 1 1 1 8 8 f . . .
                . . f 1 1 1 f 1 1 1 1 8 f . . .
                . . . f 1 1 1 1 1 1 1 1 f . . .
                . . . f 7 e e e 7 7 f f . . . .
                . . . f 7 e e 7 e 7 f . . . . .
                . . f e e 7 7 1 1 7 e f . . . .
                . . f e 7 7 f f f 7 e f . . . .
                . . . f f f . . . f f . . . . .
                """),
            img("""
                . . . f f f f f f f . . . . . .
                . . f f 8 8 6 6 8 8 f f . . . .
                . . f 8 6 6 8 6 6 8 8 f f . . .
                . . f 8 8 6 6 8 6 8 8 8 f . . .
                . . f 8 8 8 6 8 6 6 8 8 f . . .
                . . f 8 8 8 6 8 8 6 8 8 f . . .
                . . f 1 1 1 1 8 8 8 8 8 f . . .
                . . f 1 1 1 f 1 1 1 8 8 f . . .
                . . f 1 1 1 f 1 1 1 1 8 f . . .
                . . . f 1 1 1 1 1 1 1 1 f . . .
                . . . f 7 7 7 7 e e f f . . . .
                . . . f 7 e e 7 e 7 f . . . . .
                . . . f 7 e e 7 7 e f . . . . .
                . . . f e 7 7 f 1 1 f . . . . .
                . . . . f f e 7 f f . . . . . .
                . . . . . . e 7 e . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . f f f f f f . . . . . .
                . . . f 8 8 6 6 8 8 f f . . . .
                . . f 8 6 6 8 6 6 8 8 f f . . .
                . . f 8 8 6 6 8 6 8 8 8 f . . .
                . . f 8 8 8 6 8 6 6 8 8 f . . .
                . . f 8 8 8 6 8 8 6 8 8 f . . .
                . . f 1 1 1 1 8 8 8 8 8 f . . .
                . . f 1 1 1 f 1 1 1 8 8 f . . .
                . . f 1 1 1 f 1 1 1 1 8 f . . .
                . . . f 1 1 1 1 1 1 1 1 f . . .
                . . . f 7 e e e 7 7 f f . . . .
                . . . f 7 e e 7 e 7 f . . . . .
                . . f e e 7 7 1 1 7 e f . . . .
                . . f e 7 7 f f f 7 e f . . . .
                . . . f f f . . . f f . . . . .
                """)],
        500,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . f f f f f f f . . . . .
                . . f f 8 8 6 6 8 8 f f . . . .
                . f f 8 8 6 6 8 6 6 8 f . . . .
                . f 8 8 8 6 8 6 6 8 8 f . . . .
                . f 8 8 6 6 8 6 8 8 8 f . . . .
                . f 8 8 6 8 8 6 8 8 8 f . . . .
                . f 8 8 8 8 8 1 1 1 1 f . . . .
                . f 8 8 1 1 1 f 1 1 1 f . . . .
                . f 8 1 1 1 1 f 1 1 1 f . . . .
                . f 1 1 1 1 1 1 1 1 f . . . . .
                . . f f e e 7 7 7 7 f . . . . .
                . . . f 7 e 7 e e 7 f . . . . .
                . . . f e 7 7 e e 7 f . . . . .
                . . . f 1 1 f 7 7 e f . . . . .
                . . . . f f 7 e f f . . . . . .
                . . . . . e 7 e . . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f f f . . . .
                . . . . f f 8 8 6 6 8 8 f . . .
                . . . f f 8 8 6 6 8 6 6 8 f . .
                . . . f 8 8 8 6 8 6 6 8 8 f . .
                . . . f 8 8 6 6 8 6 8 8 8 f . .
                . . . f 8 8 6 8 8 6 8 8 8 f . .
                . . . f 8 8 8 8 8 1 1 1 1 f . .
                . . . f 8 8 1 1 1 f 1 1 1 f . .
                . . . f 8 1 1 1 1 f 1 1 1 f . .
                . . . f 1 1 1 1 1 1 1 1 f . . .
                . . . . f f 7 7 e e e 7 f . . .
                . . . . . f 7 e 7 e e 7 f . . .
                . . . . f e 7 1 1 7 7 e e f . .
                . . . . f e 7 f f f 7 7 e f . .
                . . . . . f f . . . f f f . . .
                """),
            img("""
                . . . . . . f f f f f f f . . .
                . . . . f f 8 8 6 6 8 8 f f . .
                . . . f f 8 8 6 6 8 6 6 8 f . .
                . . . f 8 8 8 6 8 6 6 8 8 f . .
                . . . f 8 8 6 6 8 6 8 8 8 f . .
                . . . f 8 8 6 8 8 6 8 8 8 f . .
                . . . f 8 8 8 8 8 1 1 1 1 f . .
                . . . f 8 8 1 1 1 f 1 1 1 f . .
                . . . f 8 1 1 1 1 f 1 1 1 f . .
                . . . f 1 1 1 1 1 1 1 1 f . . .
                . . . . f f e e 7 7 7 7 f . . .
                . . . . . f 7 e 7 e e 7 f . . .
                . . . . . f e 7 7 e e 7 f . . .
                . . . . . f 1 1 f 7 7 e f . . .
                . . . . . . f f 7 e f f . . . .
                . . . . . . . e 7 e . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f f f . . . .
                . . . . f f 8 8 6 6 8 8 f . . .
                . . . f f 8 8 6 6 8 6 6 8 f . .
                . . . f 8 8 8 6 8 6 6 8 8 f . .
                . . . f 8 8 6 6 8 6 8 8 8 f . .
                . . . f 8 8 6 8 8 6 8 8 8 f . .
                . . . f 8 8 8 8 8 1 1 1 1 f . .
                . . . f 8 8 1 1 1 f 1 1 1 f . .
                . . . f 8 1 1 1 1 f 1 1 1 f . .
                . . . f 1 1 1 1 1 1 1 1 f . . .
                . . . . f f 7 7 e e e 7 f . . .
                . . . . . f 7 e 7 e e 7 f . . .
                . . . . f e 7 1 1 7 7 e e f . .
                . . . . f e 7 f f f 7 7 e f . .
                . . . . . f f . . . f f f . . .
                """)],
        500,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap(sprite, otherSprite):
    info.change_score_by(3)
    if True:
        sprites.destroy_all_sprites_of_kind(SpriteKind.projectile)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

def on_down_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . f f f . . . . . . . . . . .
                . f f 8 8 8 f f f f . . . . . . .
                f 8 8 6 6 6 8 8 8 8 f f . . . . .
                . f 8 8 8 6 6 6 8 8 8 f f . . . .
                . . f 6 6 8 8 8 6 6 8 6 f f . . .
                . . f 8 6 8 8 8 8 6 8 8 6 f . . .
                . . f 8 8 1 1 1 1 1 1 8 8 f . . .
                . . f 1 1 1 1 1 1 1 1 1 1 f . . .
                . . f 1 1 1 f 1 1 f 1 1 1 f . . .
                . . f 1 1 1 f 1 1 f 1 1 1 f . . .
                . . f 1 1 1 1 1 1 1 1 1 1 f . . .
                . . . f 1 1 1 1 1 1 1 1 f . . . .
                . . e 7 f e e 7 7 7 e f 7 e . . .
                . . 7 e f e e 7 e 7 7 f e 7 . . .
                . . 1 1 f 7 7 7 e e 7 f 1 1 . . .
                . . . . . e e 7 7 7 7 . . . . . .
                . . . . . e 7 . . 7 e . . . . . .
                """),
            img("""
                . . . f f f . . . . . . . . . . .
                . f f 8 8 8 f f f f . . . . . . .
                f 8 8 6 6 6 8 8 8 8 f f . . . . .
                . f 8 8 8 6 6 6 8 8 8 f f . . . .
                . . f 6 6 8 8 8 6 6 8 6 f f . . .
                . . f 8 6 8 8 8 8 6 8 8 6 f . . .
                . . f 8 8 1 1 1 1 1 1 8 8 f . . .
                . . f 1 1 1 1 1 1 1 1 1 1 f . . .
                . . f 1 1 1 f 1 1 f 1 1 1 f . . .
                . . f 1 1 1 f 1 1 f 1 1 1 f . . .
                . . . f 1 1 1 1 1 1 e 7 f e . . .
                . . e 7 f e 7 e 7 e 1 1 e 7 . . .
                . . 7 e f e 7 e e 7 1 1 e . . . .
                . . . . f 7 7 7 7 f e 7 . . . . .
                . . . . f e e f 7 7 e . . . . . .
                . . . . f e 7 . . . . . . . . . .
                . . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . f f f . . . . . . . . . . .
                . f f 8 8 8 f f f f . . . . . . .
                f 8 8 6 6 6 8 8 8 8 f f . . . . .
                . f 8 8 8 6 6 6 8 8 8 f f . . . .
                . . f 6 6 8 8 8 6 6 8 6 f f . . .
                . . f 8 6 8 8 8 8 6 8 8 6 f . . .
                . . f 8 8 1 1 1 1 1 1 8 8 f . . .
                . . f 1 1 1 1 1 1 1 1 1 1 f . . .
                . . f 1 1 1 f 1 1 f 1 1 1 f . . .
                . . f 1 1 1 f 1 1 f 1 1 1 f . . .
                . . f 1 1 1 1 1 1 1 1 1 1 f . . .
                . . . f 1 1 1 1 1 1 1 1 f . . . .
                . . e 7 f e e 7 7 7 e f 7 e . . .
                . . 7 e f e e 7 e 7 7 f e 7 . . .
                . . 1 1 f 7 7 7 e e 7 f 1 1 . . .
                . . . . . e e 7 7 7 7 . . . . . .
                . . . . . e 7 . . 7 e . . . . . .
                """),
            img("""
                . . . f f f . . . . . . . . . . .
                . f f 8 8 8 f f f f . . . . . . .
                f 8 8 6 6 6 8 8 8 8 f f . . . . .
                . f 8 8 8 6 6 6 8 8 8 f f . . . .
                . . f 6 6 8 8 8 6 6 8 6 f f . . .
                . . f 8 6 8 8 8 8 6 8 8 6 f . . .
                . . f 8 8 1 1 1 1 1 1 8 8 f . . .
                . . f 1 1 1 1 1 1 1 1 1 1 f . . .
                . . f 1 1 1 f 1 1 f 1 1 1 f . . .
                . . f 1 1 1 f 1 1 f 1 1 1 f . . .
                . . e f 7 e 1 1 1 1 1 1 f . . . .
                . . 7 e 1 1 e 7 7 7 e f 7 e . . .
                . . . e 1 1 7 7 e 7 7 f e 7 . . .
                . . . . 7 e f 7 e e 7 f . . . . .
                . . . . . e e 7 f 7 7 f . . . . .
                . . . . . . . . . 7 e f . . . . .
                . . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_life_zero():
    game.set_game_over_message(False, "Bacons killed last guest")
    game.game_over(False)
info.on_life_zero(on_life_zero)

def on_on_overlap2(sprite2, otherSprite2):
    info.change_life_by(1)
    if True:
        sprites.destroy_all_sprites_of_kind(SpriteKind.food)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    info.change_life_by(-1)
    if True:
        sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap3)

grenade: Sprite = None
bacon: Sprite = None
medkit: Sprite = None
mySprite: Sprite = None
info.set_score(0)
info.set_life(5)
mySprite = sprites.create(img("""
        . . . . f f f . . . . . . . . . .
        . . f f 8 8 8 f f f f . . . . . .
        . f 8 8 6 6 6 8 8 8 8 f f . . . .
        . . f 8 8 8 6 6 6 8 8 8 f f . . .
        . . . f 6 6 8 8 8 6 6 8 6 f f . .
        . . . f 8 6 8 8 8 8 6 8 8 6 f . .
        . . . f 8 8 1 1 1 1 1 1 8 8 f . .
        . . . f 1 1 1 1 1 1 1 1 1 1 f . .
        . . . f 1 1 1 f 1 1 f 1 1 1 f . .
        . . . f 1 1 1 f 1 1 f 1 1 1 f . .
        . . . f 1 1 1 1 1 1 1 1 1 1 f . .
        . . . . f 1 1 1 1 1 1 1 1 f . . .
        . . . e 7 f e e 7 7 7 e f 7 e . .
        . . . 7 e f e e 7 e 7 7 f e 7 . .
        . . . 1 1 f 7 7 7 e e 7 f 1 1 . .
        . . . . . . e e 7 7 7 7 . . . . .
        . . . . . . e 7 . . 7 e . . . . .
        """),
    SpriteKind.player)
controller.move_sprite(mySprite, 100, 0)
music.play(music.create_song(hex("""
        0078000408090106001c00010a006400f401640000040000000000000000000000000000000002700104000800010a08000c00030811290c001000021e2510001400030d1e2914001800021e2518001c0001291c002000012520002400012924002800012428002c00012930003400012738003c0001243c004000021124440048000220274c005000011158005c00020f27600064000205246400680001246c0070000312202774007800011478007c00020c297c008000012580008400012984008800012588008c000212298c009000021e2590009400030c1b2994009800011e98009c00020a1b9c00a00003121e25a000a4000122a400a8000125a800ac00020822ac00b0000125b000b4000122b400b800021125b800bc000122bc00c0000125c000c4000122c400c8000125c800cc00020a22cc00d000021925d000d40003111b22d400d8000119d800dc00020d1bdc00e0000119e000e4000122e800ec00021822f000f400011ef800fc00021e2200010401011e04010801020d240c011001021e2510011401010d18011c0102161d1c0120010120
        """)),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
scene.set_background_image(img("""
    7777777777777777777777777dddddddddddddddddbdddddddddddddddddddddddddddddddddddd77777777777777777777777777777777777777777ddddddd777777777777777777777777777777777
    7777777777777777777777777ddddddddddddddddbbddddddddddd7dddddddddddddddddddddddd77777777777777777777777777777777777777777ddddddd777777777777777777777777777777777
    777777777577777777757777777ddddddddddbbbbbddddddddddd777ddddddddddddbdddddddddd7777777777777777777777757777777757777777dddbbddd777777777777777777777777777777777
    77777777777777777777777777777ddddddddddddddddddddddd7777777777ddddddbbbdddddddd7777577777777777777777777777777777777777ddddbddd777777777777777777777777777777777
    77777777777777777777777777777dddddddddddddddd77777d77757777777ddddddddbbddddddd7777777777777777777777777777777777227777ddddbdddd77777777777722777777777777777777
    777777777777777777777777777777ddddddddddddd7777777777777777777dddddddddbddddddd777777777777777577777777777777772ff27777ddddbdddd77777777777722777777777777777777
    7777777777777777777777777777777dddddddddd77777777777777777777ddddddddddbddddddd77777777757777777577777777577772fff2777dddddbdddd7777777777772f777777777777777777
    77777777777777777777777777777777ddddd7777777777777777777777ddddddddddddbddddddd777777777777777777777777777777722222777dddddbddddd7777757777722777777777777777777
    77777777777777777777777777777777ddd777777777777777777777777dddddddddddddbdddddd777777777777777777777777777777277777777dddddbddddd7777777777777777777775777777777
    77777777775777777777777777777777ddd7777777777777777222f777ddddddddddddddbbddddd77777777777777777777777777777777777777ddddddbdddddd777777777777777777777777777777
    7777777777777777777777777777777dddd7777777777757777772277777777dddddddddddbddddddddd777777777777777777777777757777777ddddddbdddddd777777777777777777777777777777
    7757777777777777777777577777ddddddd777777777777777777777777777777ddddddddddbdddddddddddd77777777227777777777777777777ddddddbddddddd77777777777577777777777777777
    777777777777777777777777777dddddddd7777777777777777777777777777777777ddddddbddddddddddddd7777772ff2777777777777777777ddddddbddddddd77777777777777777777777777777
    777777777777775777777777777dddddddd777577777777777777777777777777777dddddddbbdddddddddddd777777ff27777777777777777777ddddddbddddddd77777777777777777777777777777
    777777777777777777777777777dddddddd777777777777777777777777777777777ddddddddbdddddddddddd777777777777777777777777777dddddddbdddddd777777777777777777777777777777
    7777777777777777777777777777ddddddd777777777777777577777777777777777dddddddddbddddddddddd7777777777777777777777777dddddddddbddddd7777777777777777777757777777777
    7777777777777777777777777777ddddddd777777777777777777777777777777777ddddddddddbdddddddddd77777777777777777777777dddddddddddbddd777777777777777777777777777777777
    777777777777777777777f2777777dddddd777777777777777777777777777777777ddddddddddbdddddddddd7777777777777777777ddddddddbddddddbdd7777777777777777777777777777777777
    777777777777777777772ff7777777dddddd777777777777222777777775777777777dddddddddbbdddddddd7777775777777777dddddddddddbdddddddb777777777777777777777777777777777777
    777777777777777777772ff27777777ddbdd7777777777772ff777777777777775777ddddddddddbdddddddd77777777777777dddddddddddddbdddddddb777777777777777777777777777777777777
    7777777777777777777522277777777ddbdd7777777777722fff77777777777777777ddddddddddbdddddddd777777777dddddddddddddddddbddddddddb777777777777777777777777777777777777
    7777777777775777777772777777777dbbdd777777777777227777777777777777777ddddddddddbdddddddd77777ddddddddddddddddddddbdddddddddb777777777777775777777777777777777777
    7777777777777777777772777777777dbddd7777777757777777777777777777777777ddddddddddbddddddddddddddddddddddddddddddddbdddddddddb777777777777777777777777777777777777
    777777777777777777777777777777dbdddd777777777777777777777777777777777777ddddddddbdddddddddddddddddddddddddddddddbddddddddddb777777777777777777777777777777777777
    777777577777777777777777777777bddddd777777777777777777777777777777777777ddddddddbdddddddddddddddddddddddddddddddbdddddddddbd777777777777777777777777777777777777
    77777777777777777777777777777dbddddd7777777777777777777777777777777777777dddddddbddddddddddddddddddddddddddddddbddddddddddbd777777777777777777777777777777777777
    7777777777777777777777777777dbbddddd77777777777777777777777777222777777777ddddddbddddddddddddddddddddddddddddddbddddddddddbd777777777777777777777777777777777777
    77777777777777777777777777dddbdddddd7777777775777777777777777722277777777dddddddbdddddddddddddddddddddddddddddbdddddddddddbd777577777777777777777777757777777777
    7777777777777777777777777ddddbddddddd777777777777777777577777722ff777777ddddddddbdddddddddddddddddddddddddddddbdddddddddddbd777777777777777777722227777777777777
    7772277777777777777777dddddddbddddddd7777777777777777777777777772277777dddddddddbdddddddddddddddddddddddddddddbdddddddddddbd7777777777777777772fff22777777777777
    777f2277777777777777777ddddddbddddddd777777777777777777777777777777777ddddddddddbddddddddddddddddddddddddddddbddddddddddddbdd77777777777777777222227777777777777
    777ff2777777777777777777dddddbdddddd7777777777777777777777777777777777ddddddddddbdddddddddddddbddddddddddddddbddddddddddddbdd77777777777777577777777777777777777
    7772f2777777777777777777dddddbdddddd7777777777777777777777777777777777ddddddddddbdddddddddddddbdddddddddddddbdddddddddddddbddd7777777577777777777777777777777777
    777227777777775777777777ddddddbddddd777777777777777777777777777777777dddddddddddbdddddddddddddbdddddddddddddbddddddddddddbdddd7777777777777777777777777777777777
    77777777777777777777777dddddddbddddd777777777577777777777777777777777dddddddddddbddddddddddddddbdddddddddddbdddddddddddddbdddd7777777777777777777777777777777777
    77777777777777777777ddddddddddbddddd777777777777777777777777777777777dddddddddddbddddddddddddddbdddddddddddbdddddddddddddbddddd777777777777777777777777777777777
    7777777777777777777dddddddddddbddddd777777777777777777777777777777777dddddddddddbddddddddddddddbdddddddddddbdddddddddddddbddddd777777777777777777777777777777777
    77777775777777777777777777777ddbdddd777777777777777777777777577777777dddddddddddbddddddddddddddbdddddddddddbdddddddddddddbddddd777777777777777777777777777777777
    777777777777777777777777777777dbdddd7777777777777777777777777777777777ddddddddddbddddddddddddddbddddddddddbddddddddddddddbddddd777777777777777777777777777777777
    777777777777777777777777777777dbdddd7777f2777777777777dd77777777777777ddddddddddbddddddddddddddbddddddddddbddddddddddddddbddddd777777777777777777777777777777777
    7777777777777777777777777777777bdddd7777f2777777777777dddd777777777dddddddddddddbddddddddddddddbdddddddddbddddddddddddddbdddddd777777777777777777777777777777777
    7777777777777777777777777777777bdddd777722777777777777ddddddddddddddddddddddddddbddddddddddddddbdddddddddbddddddddddddddbdddddd7777777777777777777772ff777777777
    7777777777777777777777777777777dbddd777727777777777777ddddddddddddddddddddddddddbddddddddddddddbddddddddbdddddddddddddddbdddddd7777777777777777777522ff777777777
    7777777777777777777777777777777dbdddd77777777777777777dddddddddddddddddddddddddbdddddddddddddddbddddddddbdddddddddddddddbddddddd77777777777777777777222777777777
    7777777777777777777777777777777dbdddd777777777757777777ddddddddddddddddddddddddbdddddddddddddddbddddddddbdddddddddddddddbddddddd77777777777777777777727777777777
    7777777777777777777777777777777ddbddd777777777777777777ddddddddddddddddddddddddbddddddddddddddbdddddddddbddddddddddddddddddddddd77777772777777777777777777777777
    7777777777777777777777777777777ddbddd77777777777777777dddddddddddddddddddddddddbddddddddddddddbddddddddbdddddddddddddddddddddddd7777777f227777777777777777777777
    7777777777777777777777577777777ddbddd7777777777777777dddddddddddddddddddddddddbddddddddddddddbdddddddddbddddddddddddddddddddddd77777777ff27777777777777777777777
    7777777777777757777777777777777ddbdddd77777777777777ddddddddddbbbbbbbbbbbbbbbbddddddddddddddbdddddddddbdddddddddddddddddddddddd77777777ff27777777777777777777777
    7777777777777777777777777777777dddbdddd777777777777dddddddddbbddddbbbbbbbbbddddddddddddddddbdddddddddbdddddddddddddddddddddddddd77777572277777777777777777777777
    7777777777777777777777777777777ddddbddddd7777777777ddddddddbbdddbbdddddddddbdddddddddddddddbdddddddddbdddddddddddddddddddddddddd77777777777777777777777777777777
    7777777577777777777777777777777ddddbddddddd77777777dddddddbddbbbdddddddddddbdddddddddddddddbddddddddbddddddddddddddddddddddddddd77777777777777777777777777757777
    7777777777775777222777777777777ddddbdddddddd7777777dddddddbbbddddddddddddddbdddddddddddddddbddddddddbddddddddddddddddddddddddddd77777777777777777777777777777777
    77777777777777772f2777777777777ddddbdddddddd777777dddddddbbddddddddddddddddbddddddddddddddbddddddddbddddddddddddddddddddddddddddd7777777777777777777777777777777
    777777777777777722277777777777ddddddbdddddddd7777dddddddbbdddddddddddddddddbddddddddddddddbdddddddddddddddddddddddddddddddddddddd7777777777777777777777777777777
    777777777777777722277777777777ddddddbddddddddddddddddddbdbddddddddddddddddddbdddddddddddddbddddddddddddddddddddddddddddddddddddddd777777777777777777777777777777
    777777777777777777777777777777ddddddbddddddddddddddddddbbdddddddddddddddddddbddddddddddddbddddddddddddddddddd7777ddddddddddddddddd777777777777777777777777777777
    777777777777777777777777777777ddddddbdddddddddddddddddbbddddddddddddddddddddbddddddddddddbddddddddddddddddddd777777ddddddddddddddd777777777777777777777777777777
    777777777777777777777777777777ddddddbdddddddddddddddddbddddddddddddddddddddddbddddddddddbddddddddddddddddddd777777777777dddddddddd777777777757777777777777777777
    777777777777777777777777777777ddddddbddddddddddddddddddddddddddddddddddddddddbddddddddddbdddddddddd7dddddddd777777777777dddddddddd777777777777777777777777777777
    777777777777777777777777777777dddddbdddddddddddddddddddddddddddddddddddddddddbdddddddddbddddddddddd77ddddddd777777777777dddddddddd777777777777777775777777777777
    777777777777777777777775777777dddddbddddddddddddddddddddddddddddddddddddddddddbddddddddbddddddddddd777dddddd7777777777777ddddddddd777777777777777777777777777777
    777777777777777777777777777777dddddbddddddddddddddddddddddddddddddddddddddddddbdddddddbdddddddddddd7777ddddd7777757777777ddddddddd777777777777777577777777777777
    7777777777777777777777777777777ddddbdddddddddddddddddddddddddddddddddddddddddddbddddddbdddddddddddd77777ddddd777777777777ddddddddd777777777777777777777777777777
    7777777777777777777777777777777ddddbddddddddddddddddddddddddddddddddddddddddddddbdddddbdddddddddddd77757ddddd777777777777ddddddddd777777777777777777777777777777
    7777777777777777777777777777777ddddbddddddddd77dddddddddddddddddddddddddddddddddbdddddbdddddddddddd777777dddd777777777777ddddddddd777777777777777777777777777777
    7777777777777777777777777777777ddddbdddddddd777dddddddddddddddddddddddddddddddddbdddddbddddddddddd77777777ddd777777777777ddddddddd777777777777777777775777777777
    7777777777777777777777777777777ddddbddddddd7777ddddddddddddddddddddddddddddddddddbddddbddddddddddd777777777dd77777777777dddddddddd777777777777777777777777777777
    7777777757777777777777777777777ddddbddddddd7777ddddddd777ddddddddddddddddddddddddbddddbddddddd77dd7777777277d77777777777dddddddddd777775777777777777777777777777
    777777777777777777577777dd7777dddddbddddddd77777dddd77777777dddddddddddddddddddddbddddbddddd7777777777777227577777777777dddddddddd777777777777777777777777777777
    777777777777777777777777ddddddddddbddddddd777777ddd77777777777dddddddddddddddddddbddddbdddd77777777777772f2777777777777ddddddddddd777777777777777777777777777777
    7777777777777777777777777dddddddddbdddddd7777777dd77777777777777dddddddddddddddddbddddbddd777777777777777ff777777777777dddddddddddd77777777777777777777777777777
    7777777777777777777777777dddddddddbddddd77777777dd777777277777777ddddddddddddddddbddddbdd777777777777777777777777777777dddddddddddd77777777777777777777777777777
    7777777777777777777777777dddddddddbddddd77777777777777772f777777777ddddddddddddddbddddbdd777777777757777777777777777777dddddddd777777777777777777777777777777777
    7777777777777777777777777dddddddddbddddd7777777775777777ff2777777777ddddddddddddbdddddddd777777777777777777777777777777ddddd777777777777777777777777777777777777
    7777777777777777777777777dddddddddbdddd77777777777777777227777777777ddddddddddddbdddddddd777777777777777777777777777777dddd7777777777777777777777777777777777777
    7777777777777777777777777dddddddddbdddd77777777777777777777777777777ddddddddddddbdddddddd777777777777777777777777777777dddd7777777777777777777777777777777777777
    77727777777777777777777777ddddddddbdddd777775777777777777777777777777ddddddddddbddddddddd777777777757777777777757777777dddd7777777777777777777777777777777777777
    77222777777777777777777777ddddddddddddd777777777777777777775777777777dddddddddbdddddddddd77777777777777777777775777777ddddd7777777777777777777777577777777777777
    777ff777777777777777777777ddddddddddddd7777777777777777777777777777777dddddddbdddddddddd775777777777777772227777777777ddddd7777777777777777777777777777777777777
    7772f777577777777777777777ddddddddddddd7777777777777777777777777777777dddddddbdddddddddd777777777777777722f27777777777ddddd7777777777777777777777777777777777777
    777727777777777777777777777dddddddddddd77777777777777777777777777777777ddddbbddddddddddd777722777777777722f27777777777ddddd7777777777777777777777777777777777777
    777777777777777777777777777ddddddddddd777777777777777777772227777777777dddbddddddddddddd777fff277777777772277777777777dddddd777757777777222777777777777777777777
    7777777777777777777777777777dddddddddd777777777777577777772222777777777ddbdddddddddddddd777ff2f27777777777777777757777dddddd7777777775772ff777777777777777777777
    7777777777777777777777777777dddddddddd7777772777777777777772f2777777777ddbdddddddddddddd777722277777777777777777777777ddddddd777777777772ff777777777777777777777
    7777777777777777777777722277dddddddddd777772227777777777777222777777777dbdddddddddddddddd77777777777777777777777777777dddddddd7777777777222777777777777777777777
    777777777777777777777772f227ddddddddd7777772f7777777777777777777777777ddbdddddddddddddddd777777777777777777777777777777ddddddd7777777777727777777777777777777777
    7777777777777777775777722227ddddddddd77777777777777777777777777777777ddbddddddddddddddddddd7777777777777777577777777777ddddddd7777777777777777777777777777777777
    77777777777777777777777777777dddddddd7777777777777777777777777777777dddbddddddddddddddddddd7777777777777777777777777777ddddddd7777777777777777777777777777777777
    77777577777777777777777777777dddddddd777777777777777777777777777777dddbdddddddddddddddddddddd77777777777777777777777777ddddddd7777777777777777777777727777777777
    77777777777777777777777777777ddddddddd7777777777777777777777777777dddbdddddddddddddddddddddddd7777777777777777772222777dddddddd777777777777777777777222777777777
    77777777777777777777777777777ddddddddd777777777777777777577777777ddddbddddddddddddddddddddddddd7777777777777577722ff7777ddddddd777777777777777777777fff777777777
    77777777777777777777777777777ddddddddd77777777777777777777777777ddddbddddddddddddddddddddddddddddd77777777777777722f7777ddddddd777777777777777777777fff277777777
    77777777775777777777777777777ddddddddddd77777777577777777777777dddddbddddddddddddddddddbdddddddddddd77777777777772227777ddddddd7777777777777757777772ff277777777
    77777777777777777777777777777dddddddddddd7777777777777777777777dddddbdddddddddddddddddddbbdddddddddddd777777777777777777ddddddd777777777777777777777222777777777
    777777777777777777777777777777ddddddddddd7777777777777777777777dddddbdddddddddddddddddddddbddddddddddddd7777777777777777ddddddd777777777777777777777772777777777
    7777777777777777777777777777777dddddddddddd7777777777777777777dddddbdddddddddddddddddddddddbbddddddddddddd7777777777777ddddddd7777777777777777777777777777777777
    7777777777777777777777777777777ddddddddddddddd7777777777777777dddddbdddddddddddddddddddddddddbddddddddddddddd777777777dddddddd7777777777777777777777777777775777
    7777777777777777777777777777777ddddddddddddddddd7777777777777ddddddbdddddddddddddddddddddddddbbbbbbbbdddddddddddd7777ddddddddd7777777777777777777777777777777777
    7777777777777777777777777777777ddddddddddddddddddd7777777777dddddddbdddddddddddddddddddddddddddddddddbbbdddddddddddddddddddddd7777777777777777777777777777777777
    7777772777777777777777777777777ddddddddddddddddddd777777777dddddddddddddddddddddddddddddddddddddddddddddbddddddddddddddddddddd7777777777777777777777777777777777
    777777227777577777777777577777ddddddddddddddddddddd7777777dddddddddddddddddddddddddddddddddddddddddddddddbdddddddddddddddddddd7777777777777777777777777777777777
    757777f27777777777777777777777ddddddddddddddddddddd7777ddddddddddddddddddddddddddddddddddddddddddddddddddbddddddddddddddddddddd777777777777777777777777777777777
    777777ff77777777777777777777dddddddddddddddddddddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddbdddddddddddddddddddd777777775777777777777777777777777
    7777772277777777777777777777ddddddddddddddddddddddddddddddbbddddddddddddddddddddddddddd7777777777777777777dbbdddddddddddddddddd777777777777777777777777777777777
    777777227777777777777777777ddddddddddddddddddddddddddddddbdbdddddddddddddddddddddddd77777777777777777777777ddbdddddddddddddddddd77777777777777777577777777777777
    77777777777777777777777777dddddddddddddddddddddddddddddbbbbbdddddddddddddddddd777777777777777777777727757777dbdddddddddddddddddd77777777777777777777777777777777
    77777777777777777777777777ddddddddddddddddddddddddddddbbddddddddddddddddddddd7777777775777777777777227777777ddbddddddddddddddddd77777777777777777777777777777777
    77777777777777777777777777ddddddddddddddddddddddddddbbbdddddddddddddddddddddd777777777777777777777772f7777777dbddddddddddddddddd77777777777777777777777777777777
    77777777777777777777777777ddddddddddddddddddddddddbbdbbdddddddddddddddddddddd77777777777777757777777ff7777777ddbddddddddddddddddd7777777777777777777777775777777
    77777777777777777777777777dddddddddddddbdddddbdddbbbbddddddddddddddddddddddd7777777777777777777777777757777777dbdddddddddddddddd77777777777777777777777777777777
    77777777777777777777777777ddddddddddddbbdddbbbbbbbbddddddddddddddddddddddddd77777777777777777777777777777777777dbddddddddddddddd77777777777777777777777777777777
    77777777777777777777777777ddddddddddddbbddbbdddddddddddddddddddddddddddddddd777777777ff277777577777777777777777dbddddddddddddddd77777775777777777777777777777777
    777777777777757777777777777ddddddddddbbbdbbddddddddddddddddddddddddddddddddd777777777ff2777777777777772777777777dbddddddddddddddd77777777fff77777777777777777777
    777777577777777777777777777ddddddddddbdbbbdddddddddddddddddddddddddddddddddd7777777777ff277775777777772f77577777dbddddddddddddddd77777777fff27777777777777777777
    777777777777777777777777777ddddddddddbdbbbdddddddddddddddddddddddddddddddddd77775777772f777777777777777ff5777777ddbddddddddddddddddd7777772227777777777777777777
    777777777777777777777777777ddddddddddbdddddddddddddddddddddddddddddddddddddd7777777777777777777777777772777777777ddbdddddddddddddddd7777777777777777777777777777
    777777777777777777777777777ddddddddddbdddddddddddddddddddddddddddddddddddddd77777777777777777777777777777777777777dbddddddddddddddd77777777777777777777777777777
    777777777777777777777777777ddddddddddbdddddddddddddddddddddddddddddddddddddd777777777777777777777777777777777777777bddddddddddddd7777777777777777777777777777777
    777777777777777777777777777ddddddbddddddddddddddddddddddddddddddddddddddddddd77777777777777777777777777777777777777dddddddddddddd7777777777777777777777777777777
    """))
scene.camera_follow_sprite(mySprite)
tiles.set_current_tilemap(tilemap("""
    level4
    """))
mySprite.say_text("grab grenades each grenade is 3 points you need 250 points to win ",
    5000,
    True)

def on_forever():
    scroller.scroll_background_with_camera(scroller.CameraScrollMode.BOTH_DIRECTIONS)
    scroller.scroll_background_with_speed(0, 50)
forever(on_forever)

def on_forever2():
    global medkit
    medkit = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . .
            . . . . . . d d d d d . . . . . .
            . . . . . d d . . . d d . . . . .
            . . . . . d . . . . . d . . . . .
            . . . 1 1 1 1 1 1 1 1 1 1 1 . . .
            . . 1 1 1 1 1 1 1 1 1 1 1 1 1 . .
            . . 1 1 1 1 1 1 2 1 1 1 1 1 1 . .
            . . 1 1 1 1 1 1 2 1 1 1 1 1 1 . .
            . . 1 1 1 1 2 2 2 2 2 1 1 1 1 . .
            . . 1 1 1 1 1 1 2 1 1 1 1 1 1 . .
            . . 1 1 1 1 1 1 2 1 1 1 1 1 1 . .
            . . 1 1 1 1 1 1 1 1 1 1 1 1 1 . .
            . . . 1 1 1 1 1 1 1 1 1 1 1 . . .
            . . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . . .
            """),
        mySprite,
        0,
        50)
    medkit.set_kind(SpriteKind.food)
    medkit.y = randint(15, 0)
    pause(10000)
forever(on_forever2)

def on_forever3():
    global bacon
    bacon = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
            . . . . e e e e e e e e . . . .
            . . . e e 4 4 e e 4 e e e . . .
            . . e 4 4 4 e 4 4 4 4 4 e e . .
            . . e 4 e e e 4 e e e 4 4 e . .
            . e 4 e 1 e 4 4 1 1 e e 4 e . .
            . e e e 1 1 e 1 1 1 e e 4 e . .
            . . f e 1 1 1 1 1 1 1 e e e . .
            . . f e 1 1 f 1 1 f 1 1 1 f . .
            . . f b b b b b b b b b b f . .
            . . . f b b b b b b b b f . . .
            . . c c f c b b b b c f c c . .
            . . 1 1 f c c 9 b c c f 1 1 . .
            . . 1 1 f c c 9 9 c c f 1 1 . .
            . . . . . f f f f f f . . . . .
            . . . . . f f . . f f . . . . .
            """),
        mySprite,
        0,
        50)
    bacon.set_kind(SpriteKind.enemy)
    bacon.y = randint(15, 0)
    pause(3000)
forever(on_forever3)

def on_forever4():
    global grenade
    grenade = sprites.create_projectile_from_sprite(img("""
            . . . . . . . f f f f f f f . .
            . . . . . . f b b b d d d d f .
            . . . . . . f b b b d . . d f .
            . . . . . f b b b b d d . d f .
            . . . . . f 7 f 7 f 7 d d d f .
            . . . . f 7 7 f 7 f 7 7 f f . .
            . . . . f f f f f f f f f . . .
            . . . . f 7 7 f 7 f 7 7 f . . .
            . . . . f f f f f f f f f . . .
            . . . . f 7 7 f 7 f 7 7 f . . .
            . . . . f f f f f f f f f . . .
            . . . . . f 7 f 7 f 7 f . . . .
            . . . . . . f f f f f . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        mySprite,
        0,
        50)
    grenade.set_kind(SpriteKind.projectile)
    grenade.y = randint(15, 0)
    pause(2000)
forever(on_forever4)

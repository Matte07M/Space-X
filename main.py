def on_a_pressed():
    global dart
    dart = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . 8 f f 8 8 8 f f . . . . . . 
                    . . 5 5 5 5 5 5 5 5 5 5 . . . . 
                    . . 4 f f f f f f f f 4 4 8 . . 
                    . . 2 2 2 2 2 2 2 2 8 2 2 2 2 2 
                    . . 4 f f f f f f f f 4 4 8 . . 
                    . . 5 5 5 5 5 5 5 5 5 5 5 . . . 
                    . . 8 f f 8 8 8 f f . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        plane,
        200,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy()
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

bogey: Sprite = None
dart: Sprite = None
plane: Sprite = None
plane = sprites.create(img("""
        ....................
            ....................
            ....................
            ....ffffff..........
            ..2f888888ffff......
            .42f8888866669f.....
            542f88886666699f....
            542f888866666999f...
            542fffffffffffffffff
            542f888866666999f...
            542f88886666699f....
            .42f8888866669f.....
            ..2f888888ffff......
            ....ffffff..........
            ....................
            ....................
            ....................
            ....................
            ....................
            ....................
    """),
    SpriteKind.player)
plane.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
info.set_life(3)
controller.move_sprite(plane, 200, 200)

def on_update_interval():
    global bogey
    bogey = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 7 5 . . . . . . . 
                    . . . . . 7 7 f f f f f f f f f 
                    . . . . 7 5 5 5 8 5 5 8 5 4 5 5 
                    . . . . 2 5 5 4 4 5 5 d d d 5 5 
                    . . . f 7 7 7 7 8 d d 4 4 d 7 7 
                    . . f 2 7 2 2 2 d d d d d 2 2 2 
                    . . f 2 2 7 7 4 8 7 7 8 4 4 4 4 
                    . . . f 5 5 5 5 5 5 5 5 5 5 5 5 
                    . . . . f f f f f f f f f f f f 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    bogey.set_velocity(-100, 0)
    bogey.set_position(180, randint(0, 120))
game.on_update_interval(500, on_update_interval)

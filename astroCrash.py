# Rotate Sprite
# Demonstrates rotating a sprite

from livewires import games

games.init(screen_width = 780,  screen_height = 480, fps = 50)

class Ship(games.Sprite):
    ''' A rotating ship. '''
    def update(self):
        ''' Rotate based on keys pressed. '''
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += 1
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= 1

        if games.keyboard.is_pressed(games.K_1):
            self.angle = 0
        if games.keyboard.is_pressed(games.K_2):
            self.angle = 90
        if games.keyboard.is_pressed(games.K_3):
            self.angle = 180
        if games.keyboard.is_pressed(games.K_4):
            self.angle = 270


def main():
    nebula_image = games.load_image('nebula.jpg', transparent = False)
    games.screen.background = nebula_image

    ship_image = games.load_image('ship.jpg')
    the_ship = Ship(image = ship_image,
                    x = games.screen.width / 2,
                    y = games.screen.height / 2)
    games.screen.add(the_ship)

    games.screen.mainloop()

main()


#class Ship(games.Sprite):
##        ''' Move ship based on keys pressed. '''
##        if games.keyboard.is_pressed(games.K_w):
##            self.y -= 1
##        if games.keyboard.is_pressed(games.K_s):
##            self.y += 1
##        if games.keyboard.is_pressed(games.K_a):
##            self.x -= 1
##        if games.keyboard.is_pressed(games.K_d):
##            self.x += 1

# Sound And Music
# Demonstrates playing sound and music files

from livewires import games

games.init(screen_width = 780,  screen_height = 480, fps = 50)

# load a sound file (WAV only)
missile_sound = games.load_sound('missile.wav')

# load the music file
games.music.load('theme.mp3')

choice = None
while choice != '0':

    print(
        '''
Sound and Music
1 - Play missile sound
2 - Loop missile sound
3 - Stop missile sound
4 - Play theme music
5 - Loop theme music
6 - Stop theme music
'''
        )

    choice = input('Choice: ')
    print()

    # exit
    if choice == '0':
        print('Good-bye.')

    # play missile sound
    elif choice == '1':
        missile_sound.play()
        print('Playing missile sound.')

    # loop missile sound
    elif choice == '2':
        loop = int(input('Loop how many extra times? (-1 = forever): '))
        missile_sound.play(loop)
        print('Looping missile sound.')

    # stop missile sound
    elif choice == '3':
        missile_sound.stop()
        print('Stopping missile sound')

    # play theme music
    elif choice == '4':
        games.music.play()
        print('Playing theme music.')

    # loop theme music
    elif choice == '5':
        loop = int(input('Loop how many extra time? (-1 = forever): '))
        games.music.play(loop)
        print('Looping theme music.')

    # stopping the music
    elif choice == '6':
        games.music.stop()
        print('Stopping theme music.')

    # some unknown choice
    else:
        print('\nSorry, but', choice, 'isn\'t a valid choice.')

input('\n\nPress the enter key to exit.')




# SHIP MOVE WSAD
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


# SHIP ROTATE
##class Ship(games.Sprite):
##    ''' A rotating ship. '''
##    def update(self):
##        ''' Rotate based on keys pressed. '''
##        if games.keyboard.is_pressed(games.K_RIGHT):
##            self.angle += 1
##        if games.keyboard.is_pressed(games.K_LEFT):
##            self.angle -= 1
##
##        if games.keyboard.is_pressed(games.K_1):
##            self.angle = 0
##        if games.keyboard.is_pressed(games.K_2):
##            self.angle = 90
##        if games.keyboard.is_pressed(games.K_3):
##            self.angle = 180
##        if games.keyboard.is_pressed(games.K_4):
##            self.angle = 270


##def main():
##    nebula_image = games.load_image('nebula.jpg', transparent = False)
##    games.screen.background = nebula_image
##
##    ship_image = games.load_image('ship.jpg')
##    the_ship = Ship(image = ship_image,
##                    x = games.screen.width / 2,
##                    y = games.screen.height / 2)
##    games.screen.add(the_ship)
##
##    games.screen.mainloop()
##
##main()


# EXPLOSION
##explosion_files = ['explosion_01.jpg',
##                   'explosion_02.jpg',
##                   'explosion_03.jpg',
##                   'explosion_04.jpg',
##                   'explosion_05.jpg',
##                   'explosion_06.jpg',
##                   'explosion_07.jpg',
##                   'explosion_08.jpg']
##
##explosion = games.Animation(images = explosion_files,
##                            x = games.screen.width / 2,
##                            y = games.screen.height / 2,
##                            n_repeats = 0,
##                            repeat_interval = 5)
##games.screen.add(explosion)
##
##games.screen.mainloop()


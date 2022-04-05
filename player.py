import pygame
from support import map_folders, import_images, flip_animation

vector = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    """Class for the playable character"""

    def __init__(self, player_class, position):
        super().__init__()

        # Set contants
        self.HORIZONTAL_ACCELERATION = 1.5
        self.HORIZONTAL_FRICTION = 0.15
        self.VERTICAL_ACCELERATION = 0.8  # Gravity
        self.VERTICAL_JUMP_SPEED = -18  # Determines how high the player can jump
        self.STARTING_HEALTH = 100
        self.ANIMATION_SPEED = .15

        self.player_class = player_class
        self.direction = 1

        #Bring in all the animation frames
        self.import_character_assets(player_class)

        # Create the animation frames for when the player is moving left
        current_keys = self.animations.keys()
        for key in list(current_keys):
            self.animations.update({key + '_Left': flip_animation(self.animations[key])})

        #Scale up the player size
        for key in self.animations.keys():
                self.animations[key] = [pygame.transform.scale2x(image) for image in self.animations[key]]

        self.current_sprite = 0
        self.image = self.animations['Idle'][self.current_sprite]
        self.rect = self.image.get_rect(bottomleft = position)

        #Create kinematic vectors
        self.position = vector(position)
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, self.VERTICAL_ACCELERATION)

        # Set initial player values
        self.health = self.STARTING_HEALTH
        self.starting_x = position[0]
        self.starting_y = position[1]


    def import_character_assets(self, path):
        character_path = path
        self.animations = {}
        folder_list = map_folders(path)
        for folder in folder_list:
            self.animations[folder] = []
            full_path = character_path + '/' + folder
            self.animations[folder] = import_images(full_path)

    def update(self):
        self.move()

    def move(self):
        """Moves and animates the player"""
        #Set the players acceleration vector
        self.acceleration = vector(0, self.VERTICAL_ACCELERATION)

        #Make sure the player doesn't "fall through the ground"
        if self.rect.bottomleft[1] >= self.starting_y:
            self.acceleration.y = 0
            self.velocity.y = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction = 1
            self.acceleration.x = self.HORIZONTAL_ACCELERATION * self.direction
            self.animate('Run', self.ANIMATION_SPEED)
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction = -1
            self.acceleration.x = self.HORIZONTAL_ACCELERATION * self.direction
            self.animate('Run_Left', self.ANIMATION_SPEED)
        else:
            if self.direction > 0:
                self.animate('Idle', self.ANIMATION_SPEED)
            else:
                self.animate('Idle_Left', self.ANIMATION_SPEED)

        # Calculate new kinematics values
        self.acceleration.x -= self.velocity.x * self.HORIZONTAL_FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

        #Position the player based on the calculations
        self.rect.bottomleft = self.position

    def animate(self, action, speed):
        if self.current_sprite < len(self.animations[action]) - 1:
            self.image = self.animations[action][int(self.current_sprite)]
            self.current_sprite += speed
        else:
            self.current_sprite = 0
            self.image = self.animations[action][int(self.current_sprite)]
            self.current_sprite += speed
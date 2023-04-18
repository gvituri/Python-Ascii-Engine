from enum import Enum

class Sprite:
    def __init__(self, sprite_index, rotation, background_color_RGB, foreground_color_RGB) -> None:
        if sprite_index < 0 or sprite_index > 256:
            raise TypeError("The sprite index must be cointained between 0 and 256.")

        if (rotation % 90) != 0:
            raise TypeError("The sprite rotation must be divisible by 90.")
        
        for i in range(3):
            if background_color_RGB[i] < 0 or background_color_RGB[i] > 255:
                raise TypeError("Each value for RGB in the sprite background color must be cointained between 0 and 255.")
            if foreground_color_RGB[i] < 0 or foreground_color_RGB[i] > 255:
                raise TypeError("Each value for RGB in the sprite foreground color must be cointained between 0 and 255.")

        self._sprite_index = sprite_index # Sprite sheet index in which the sprite is found
        self._rotation = rotation # Rotation in radians and 90° intervals indicating the rotation in which the sprite must be rendered
        self._background_color_RGB = background_color_RGB # RGB color for the background
        self._foreground_color_RGB = foreground_color_RGB # RGB color for the background

    @property
    def sprite_index(self):
        return self._sprite_index
    
    @sprite_index.setter
    def sprite_index(self, value):
        self._sprite_index = value

    @property
    def rotation(self):
        return self._rotation
    
    @rotation.setter
    def rotation(self, value):
        self._rotation = value

    @property
    def background_color_RGB(self):
        return self._background_color_RGB
    
    @background_color_RGB.setter
    def background_color_RGB(self, value):
        self._background_color_RGB = value

    @property
    def foreground_color_RGB(self):
        return self._foreground_color_RGB
    
    @foreground_color_RGB.setter
    def foreground_color_RGB(self, value):
        self._foreground_color_RGB = value

class AnimatedSprite(Sprite):
    def __init__(self, sprite_index, rotation, background_color_RGB, foreground_color_RGB, animation_type, animation_frames) -> None:
        super().__init__(sprite_index, rotation, background_color_RGB, foreground_color_RGB)
        self._animation_type = animation_type # AnimationType Enum indicating the animation type to be played
        self._animation_frames = [Sprite(sprite_index, rotation, background_color_RGB, foreground_color_RGB)]
        self._animation_frames.extend(animation_frames) # List of Sprites to be used when animating. Frame 0 is always a clone from self
        self._current_frame = 0 # Current animation frame

    @property
    def animation_type(self):
        return self._animation_type
    
    @animation_type.setter
    def animation_type(self, value):
        self._animation_type = value
    
    @property
    def animation_frames(self):
        return self._animation_frames
    
    @animation_frames.setter
    def animation_frames(self, value):
        self._animation_frames = value

    @property
    def current_frame(self):
        return self._current_frame
    
    @current_frame.setter
    def current_frame(self, value):
        self._current_frame = value

class AnimationType(Enum):
    STATIC = 0 # No animation
    SPORADIC = 1 # Animation frame 0 has 10% chance to be the next frame
    RANDOM = 2 # Next frame is chosen randomly
    SEQUENTIAL = 3 # Next frame is 

class AnimationFrame:
    def __init__(self, sprite_index, rotation, background_color_RGB, foreground_color_RGB) -> None:
        pass
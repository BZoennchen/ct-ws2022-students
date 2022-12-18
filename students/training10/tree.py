import pygame, math
pygame.init()

def draw_tree(order, theta, size, start_position, heading, depth=0):
   branch_size = size * TRUNK_RATIO
   delta_x = branch_size * math.cos(heading)
   delta_y = branch_size * math.sin(heading)
   end_position = (start_position[0] + delta_x, start_position[1] + delta_y)
   
   pygame.draw.line(main_surface, TREE_COLOR, start_position, end_position)

   if order > 0:   
      child_size = size*(1 - TRUNK_RATIO)
      draw_tree(order-1, theta, child_size, end_position, heading-theta, depth+1)
      draw_tree(order-1, theta, child_size, end_position, heading+theta, depth+1)


def animationLoop():
    theta = 0.4
    dt = SPEED
    while True:

        # Listen to user input
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        # Update the angle
        theta += dt
        if math.pi/5 < theta or theta < -math.pi/5:
            dt *= -1
            
        # Draw everything
        main_surface.fill(BACKGROUND_COLOR)
        draw_tree(DEPT, theta, SURFACE_SIZE*0.9, (SURFACE_SIZE//2, SURFACE_SIZE-50), -math.pi/2)

        pygame.display.flip()
        my_clock.tick(120)


if __name__ == '__main__':
    # Constants
    SURFACE_SIZE = 800
    BACKGROUND_COLOR = (0, 0, 0)
    TREE_COLOR = (255, 255, 255)
    TRUNK_RATIO = 0.2
    DEPT = 12
    SPEED = 0.00
    
    main_surface = pygame.display.set_mode((SURFACE_SIZE,SURFACE_SIZE))
    my_clock = pygame.time.Clock()
    
    # Start animation
    animationLoop()
    pygame.quit()
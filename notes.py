# rect1.colliderect(rect2) # determines if one rectangle collides with another rectangle
# ex. player_rect.colliderect(snail_rect) # returns 0 for no collision or 1 for collision

# test_surface = pygame.Surface((100,200))
# test_surface.fill('Red') # changes surface bkgd color to red
# blit stands for [bl]ock [i]mage [t]ransfer

# {PYGAME EVENTS}
# QUIT              none
# ACTIVEEVENT       gain, state
# KEYDOWN           key, mod, unicode, scancode
# KEYUP             key, mod, unicode, scancode
# MOUSEMOTION       pos, rel, buttons, touch
# MOUSEBUTTONUP     pos, button, touch
# MOUSEBUTTONDOWN   pos, button, touch
# JOYAXISMOTION     joy (deprecated), instance_id, axis, value
# JOYBALLMOTION     joy (deprecated), instance_id, ball, rel
# JOYHATMOTION      joy (deprecated), instance_id, hat, value
# JOYBUTTONUP       joy (deprecated), instance_id, button
# JOYBUTTONDOWN     joy (deprecated), instance_id, button
# VIDEORESIZE       size, w, h
# VIDEOEXPOSE       none
# USEREVENT         code

# rectangles are used primarily for positioning, collisions, and drawing

# pygame.draw
# draw rectangles, circles, lines, points, ellipses, etc

# installato ed importato pygame e le funzioni time e random
import pygame
import time
import random
import sys

# importati i font da pygame
pygame.font.init()

# settate le variabili di l'altezza e la larghezza dello schermo di gioco
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


# settata il nome della schermata di gioco
pygame.display.set_caption("Space Dodge")


# importata immagine di background ed aggiustata per la dimensione dello schermo tramite il metodo transform.scale
try:
    BG = pygame.transform.scale(pygame.image.load(
        "IMG_9504_2.JPG"), (WIDTH, HEIGHT))
except pygame.error as e:
    # Se l'immagine non può essere caricata, crea un colore di sfondo predefinito
    BG = pygame.Surface((WIDTH, HEIGHT))
    BG.fill((0, 0, 0))  # Colore nero di sfondo

# settate le dimensioni del personaggio
PLAYER_WIDTH = 40

PLAYER_HEIGHT = 50

# settate le VELOCITA del personaggio
PLAYER_VELOCITY = 5

PROJECTILE_WIDTH = 10
PROJECTILE_HEIGHT = 15
PROJECTILE_VEL = 2

# settato quale font utilizzare e la grandezza
FONT = pygame.font.SysFont("sanserif", 30)


# creata funzione draw per riempire la schermata usando l'immagine importata
def draw(player, elapsed_time, projectiles):
    WIN.blit(BG, (0, 0))

    # stampato il tempo che scorre sullo schermo
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, (200, 100, 20), player)

    for projectile in projectiles:
        pygame.draw.rect(WIN, (200, 20, 200), projectile)

    pygame.display.update()


# Funzione principale del gioco
def main():

    run = True

    # aggiunta funzione per posizionare il personaggio in fondo allo schermo
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT,
                         PLAYER_WIDTH, PLAYER_HEIGHT)

    # aggiunto oggetto clock per regolare la velocita dei fotogrammi del gioco
    clock = pygame.time.Clock()

    start_time = time.time()
    elapsed_time = 0

    projectile_add_increment = 2000
    projectile_count = 0

    projectiles = []

    hit = False


# Aggiunto questo ciclo while per chiudere il gioco premento la X dello schermo in alto a destra
    while run:

        # settati i fotogrammi del gioco
        projectile_count += clock.tick(50)

        elapsed_time = time.time() - start_time

        if projectile_count > projectile_add_increment:
            for _ in range(3):
                projectile_x = random.randint(0, WIDTH - PROJECTILE_WIDTH)
                projectile = pygame.Rect(
                    projectile_x, - PROJECTILE_HEIGHT, PROJECTILE_WIDTH, PROJECTILE_HEIGHT)
                projectiles.append(projectile)

            projectile_add_increment = max(200, projectile_add_increment - 50)
            projectile_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

# AGGIUNTo ascolto della prumuta delle freccette per muovere il personaggio sull'asse x e y ed aggioto anche variabile per non far uscire fuori dai bordi
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY >= 0:
            player.x -= PLAYER_VELOCITY
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VELOCITY + player.width <= WIDTH:
            player.x += PLAYER_VELOCITY
        if keys[pygame.K_UP] and player.y - PLAYER_VELOCITY >= 0:
            player.y -= PLAYER_VELOCITY
        if keys[pygame.K_DOWN] and player.y + PLAYER_VELOCITY + player.height <= HEIGHT:
            player.y += PLAYER_VELOCITY

        for projectile in projectiles[:]:
            projectile.y += PROJECTILE_VEL
            if projectile.y > HEIGHT:
                projectiles.remove(projectile)
            elif projectile.y >= player.y and projectile.colliderect(player):
                projectiles.remove(projectile)
                hit = True
                break

        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width() /
                     2, HEIGHT/2 - lost_text.get_height()/2))

            pygame.display.update()
            pygame.time.delay(4000)
            break

    # aggiunta la funzione draw nella funzione principale, ed aggiunta la funzione player
    draw(player, elapsed_time, projectiles)

    pygame.quit()

    sys.exit()


# aggiunto per far partire il gioco utilizzando direttamente il codice sopra e si assicura che non viene importato
if __name__ == "__main__":
    main()

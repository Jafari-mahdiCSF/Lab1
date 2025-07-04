import psycopg2
import csv
from config import config

def create_table():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL UNIQUE
        )
        """,
    )
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
        print("PhoneBook table created successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_user_console():
    first_name = input("Enter user first name: ")
    phone = input("Enter user phone: ")
    sql = """INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (first_name, phone))
        conn.commit()
        cur.close()
        print("User added to phonebook.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_from_csv(filename):
    sql = """INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                cur.execute(sql, (row[0], row[1]))
        conn.commit()
        cur.close()
        print("Data uploaded from CSV.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def update_user():
    choice = input("Update (1) Name or (2) Phone? ")
    if choice == "1":
        phone = input("Enter phone to find user: ")
        new_name = input("Enter new name: ")
        sql = """UPDATE phonebook SET first_name = %s WHERE phone = %s"""
        values = (new_name, phone)
    elif choice == "2":
        name = input("Enter user name: ")
        new_phone = input("Enter new phone: ")
        sql = """UPDATE phonebook SET phone = %s WHERE first_name = %s"""
        values = (new_phone, name)
    else:
        print("Invalid choice.")
        return

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        print("Record updated.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def query_data():
    print("Query Options: 1) All, 2) By Name, 3) By Phone Prefix")
    choice = input("Choose: ")
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        if choice == "1":
            cur.execute("SELECT * FROM phonebook")
        elif choice == "2":
            name = input("Enter name: ")
            cur.execute("SELECT * FROM phonebook WHERE first_name = %s", (name,))
        elif choice == "3":
            prefix = input("Enter phone prefix: ")
            cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (prefix + '%',))
        else:
            print("Invalid choice.")
            return
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def delete_user():
    print("Delete by: 1) Name or 2) Phone")
    choice = input("Choose: ")
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        if choice == "1":
            name = input("Enter name: ")
            cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
        elif choice == "2":
            phone = input("Enter phone: ")
            cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
        else:
            print("Invalid choice.")
            return
        conn.commit()
        print("Record deleted.")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def main():
    while True:
        print("\nPhoneBook Menu")
        print("1. Create table")
        print("2. Insert user from console")
        print("3. Upload from CSV")
        print("4. Update user")
        print("5. Query data")
        print("6. Delete user")
        print("7. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            create_table()
        elif choice == "2":
            insert_user_console()
        elif choice == "3":
            filename = input("CSV filename: ")
            insert_from_csv(filename)
        elif choice == "4":
            update_user()
        elif choice == "5":
            query_data()
        elif choice == "6":
            delete_user()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()


#  ////////////////////////////////////////////  SNAKE GAME WITH DATABASE ///////////////////////////////////////////////////
import pygame
import random
import sys
import time
import psycopg2
from config import config

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# ----------------- DB functions ------------------------
def create_connection():
    params = config()
    conn = psycopg2.connect(**params)
    return conn

def get_or_create_user(username):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username=%s", (username,))
    user = cur.fetchone()
    if user:
        user_id = user[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
    cur.close()
    conn.close()
    return user_id

def get_last_user_state(user_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT level, score FROM user_scores WHERE user_id=%s ORDER BY saved_at DESC LIMIT 1", (user_id,))
    last_state = cur.fetchone()
    cur.close()
    conn.close()
    return last_state if last_state else (1, 0)

def save_user_state(user_id, level, score):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO user_scores (user_id, level, score) VALUES (%s, %s, %s)",
                (user_id, level, score))
    conn.commit()
    cur.close()
    conn.close()

# ----------------- Game setup --------------------------
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
BLOCK_SIZE = 20
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game with Levels & DB")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 20)

# ----------------- Username & Load State ---------------
username = input("Enter your username: ")
user_id = get_or_create_user(username)
level, score = get_last_user_state(user_id)
FPS = 10 + (level - 1) * 2

print(f"Welcome {username}! Last saved state -> Level: {level}, Score: {score}")
print("Starting in 5 seconds...")
time.sleep(5)

# ----------------- Snake & Food ------------------------
snake_pos = [[300, 300], [280, 300], [260, 300]]
snake_dir = "RIGHT"
change_to = snake_dir

def spawn_food():
    while True:
        food_pos = [random.randrange(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                   random.randrange(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE]
        if food_pos not in snake_pos:
            return food_pos

food_pos = spawn_food()

# ----------------- Main Game Loop ----------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_user_state(user_id, level, score)
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and snake_dir != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and snake_dir != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_dir != "LEFT":
                change_to = "RIGHT"
            elif event.key == pygame.K_p:
                save_user_state(user_id, level, score)
                print(f"Game paused & saved at Level {level}, Score {score}. Press any key to continue.")
                paused = True
                while paused:
                    for e in pygame.event.get():
                        if e.type == pygame.KEYDOWN:
                            paused = False

    snake_dir = change_to

    # Move snake
    head = snake_pos[0].copy()
    if snake_dir == "UP":
        head[1] -= BLOCK_SIZE
    elif snake_dir == "DOWN":
        head[1] += BLOCK_SIZE
    elif snake_dir == "LEFT":
        head[0] -= BLOCK_SIZE
    elif snake_dir == "RIGHT":
        head[0] += BLOCK_SIZE

    snake_pos.insert(0, head)

    # Check if eats food
    if snake_pos[0] == food_pos:
        score += 1
        food_pos = spawn_food()
        if score % 4 == 0:
            level += 1
            FPS += 2
    else:
        snake_pos.pop()

    # Check collision with walls
    if (snake_pos[0][0] < 0 or snake_pos[0][0] >= SCREEN_WIDTH or
        snake_pos[0][1] < 0 or snake_pos[0][1] >= SCREEN_HEIGHT):
        save_user_state(user_id, level, score)
        running = False

    # Check collision with itself
    if snake_pos[0] in snake_pos[1:]:
        save_user_state(user_id, level, score)
        running = False

    # Draw
    screen.fill(BLACK)
    for block in snake_pos:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, BLACK, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE), 1)
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, BLACK, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE), 1)

    # Draw score & level
    score_text = font.render(f"{username} | Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (SCREEN_WIDTH - level_text.get_width() - 10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()


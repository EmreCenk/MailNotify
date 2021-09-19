# MailNotify

A hardware system that detects physical mail and alerts the user. We are tranforming paper into digital.

Our project has 2 components. Software and hardware.

## Inspiration 
With several institutions (including governments) still using post to communicate crucial information, and third party sellers having uncertain delivery times / vague package tracking, keeping track of what has entered your postbox has become a daily chore in life.

There is no way to know if your postbox is full, empty, has spam in it, or has a crucial letter sent by the government that needs immediate attention. We created a system that aims to solve these problems.

## What it does
Every time you receive mail in your postbox, MailNotify sends you a notification with a picture of the letter you have received. You receive the picture as an email and a text message notification. For more information and to see a history of letters delivered, you log into our website and use the dashboard. With the dashboard, you can see pictures of delivered mail, when they entered your postbox and the corresponding weight. With the website, you can access your postbox from anywhere!

## How we built it
The first component is a hardware system that detects if a letter has been inserted into the postbox. For this, we used a raspberry pi and an ultrasonic sensor. Once a letter has been placed into your postbox, the raspberry pi takes a picture of the postbox and measures the weight difference that the letter made. The picture and weight are sent to our backend API. At the backend, the picture, weight and date are stored, then sent as notifications in the form of email and SMS. All of this information can later be accessed through our login and dashboard, no matter where you are in the world.

## Challenges we ran into
We had never worked with SQL databases, CockroachDB, Twilio, or ultrasonic sensors on a raspberry pi before. Learning them was initially a challenge, but we were able to overcome it. After spending a little while learning, It turns out CockroachDB and Twilio are easy to use. It was also our second time ever working with React. Making the front-end run on multiple devices took a much longer time than we’d like to admit, but in the end, we are happy that everything is working.

## Accomplishments that we're proud of
We are proud to have created a fully functional minimum viable product. We are also proud to have learned new frameworks and languages that we had never used before.

## What we learned
We learned how to use CockroachDB, SQL databases, Twilio, Firebase authentication, using ultrasonic sensors on a raspberry pi, and automated email sending. We were also very new to React, so our React skills improved significantly as well.

## What's next for MailNotify
We would like to create a hardware design that opens letters, reads them, and directly converts them to text. With this, we will be able to create a spam filter on your postbox. On top of spam filtering, you will be able to receive all your letters as text emails, along with pictures.





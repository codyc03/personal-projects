<?php
// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect form data
    $name = htmlspecialchars($_POST['name']);   // Sanitize user input
    $email = htmlspecialchars($_POST['email']); // Sanitize user input
    $message = htmlspecialchars($_POST['message']); // Sanitize user input

    // Recipient email address
    $to = "cody.christensensc17@gmail.com"; // Replace this with the email address you want the messages sent to

    // Subject of the email
    $subject = "New message from your website contact form";

    // Email content
    $email_content = "You have received a new message from your website contact form.\n\n";
    $email_content .= "Name: $name\n";
    $email_content .= "Email: $email\n";
    $email_content .= "Message: \n$message\n";

    // Headers for the email
    $headers = "From: $email\r\n"; // Sender's email
    $headers .= "Reply-To: $email\r\n"; // Reply to the user's email
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n"; // Set content type to plain text

    // Send the email
    if (mail($to, $subject, $email_content, $headers)) {
        echo "Thank you for contacting us, $name! Your message has been sent.";
    } else {
        echo "There was an error sending your message. Please try again later.";
    }
} else {
    // If the form was not submitted via POST
    echo "Please submit the form first.";
}
?>
import smtplib
import random

class EmailVerifier:
    def __init__(self) -> None:
        self.server = "neymar21112002born@gmail.com"
        
        self.password = "xret htuj tlqy dqgy"
        self.subject = "Verify Email"
        self.last_code = None

    def is_same_code(self, verification_code: str):
        return self.last_code == int(verification_code)

    def create_verification_code(self):
        self.last_code = random.randint(100000, 999999)
        return self.last_code
    
    def generate_email_format(self, user_email: str):
        verification_code = self.create_verification_code()
        email_body = f"Verification code:\n{verification_code}\n\
            Someone tried to use this ({user_email}) email to sign up Guide4u.\
                If this was you, please use the code above to confirm your identity."
        
        return f"From: Guide4u {self.server}\nTo: {user_email}\nSubject: {self.subject}\n\n{email_body}"
    
    def send_email(self, user_email: str):
        message = self.generate_email_format(user_email)
        try:
            connection = smtplib.SMTP("smtp.gmail.com", 587)
            connection.starttls()
            connection.login(self.server, self.password)
            print("logged in...")
            connection.sendmail(self.server, user_email, message)
            print("Email has been sent!")
            connection.close()
            
        except smtplib.SMTPAuthenticationError:
            print("Unable to sign in...")

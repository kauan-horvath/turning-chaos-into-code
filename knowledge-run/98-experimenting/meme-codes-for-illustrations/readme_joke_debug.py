# HR.exe has stopped searching. Match found.
KAUAN_DATA = {
    "Email": "kauanhorvath1996@gmail.com",
    "WhatsApp": "+55 11 95492-0195",
    "Status": "Available (maybe) and Highly Caffeinated",
}


def hire_this_guy(coffee_included=True):
    if coffee_included:
        print(">> DEPLOYING OFFER...")
        for platform, link in KAUAN_DATA.items():
            print(f"fetch('{platform}') -> {link}")
        return "Welcome aboard!"

    raise Exception(
        """
        [ CRITICAL FAILURE ] Error 402: Coffee Required.
        ================================================
        > FIX ACTION : Deploy offer or send a direct message.
        > CONNECTION : https://linkedin.com/in/kauanhorvath
        ================================================
        """
    )


if __name__ == "__main__":
    hire_this_guy()

from fpdf import FPDF


class PDF(FPDF):
    def add_header(self, text):
        self.set_font("helvetica", "B", 48)
        self.set_text_color(0, 0, 0)
        header_width = self.get_string_width(text)
        self.text((self.w - header_width) / 2, 30, text)

    def add_image(self, img):
        img_width = 150
        x = (self.w - img_width) / 2
        self.image(img, x=x, y=50, w=img_width)

    def add_text_on_image(self, text):
        self.set_font("helvetica", "B", 24)
        self.set_text_color(255, 255, 255)
        text_width = self.get_string_width(text)
        self.text((self.w - text_width) / 2, 100, text)


def main():

    # Initiate
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Text: CS50 Shirtificate
    pdf.add_header("CS50 Shirtificate")

    # Image
    pdf.add_image("shirtificate.png")

    # Text: Name
    name = input("Name: ")
    pdf.add_text_on_image(f"{name} took CS50")

    # Output
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()

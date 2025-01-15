import re
import unicodedata


class Utils:
    def clean_variable_name(name):
        # Replace spaces with underscores
        name = name.replace(" ", "_")
        # Remove special characters
        name = re.sub(r"[^\w\s]", "", name)
        # Replace accented characters with their non-accented counterparts
        name = "".join(
            (
                c
                for c in unicodedata.normalize("NFD", name)
                if unicodedata.category(c) != "Mn"
            )
        )
        return name

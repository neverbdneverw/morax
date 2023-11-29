colors = {
    "black" : "#000000",
    "white" : "#ffffff",
    "fcffff": "#fcffff",
    "fafafa": "#fafafa",
    "f6f7f8": "#f6f7f8",
    "f8fafc": "#f8fafc",
    "d6d6d6": "#d6d6d6",
    "9a6e32": "#9a6e32",
    "ae8948": "#ae8948",
    "ebebeb": "#ebebeb",
    "c09451": "#c09451",
    "c7ac65": "#c7ac65",
    "4d4d4d": "#4d4d4d",
    "a6a6a6": "#a6a6a6"
}

colors_dark = {
    "black" : "#ffffff",
    "white" : "#1c1c1c",
    "fcffff": "#0d0d0d",
    "fafafa": "#101010",
    "f6f7f8": "#121212",
    "f8fafc": "#0f0f0f",
    "d6d6d6": "#404040",
    "9a6e32": "#754123",
    "ae8948": "#6c552e",
    "ebebeb": "#2a2a2a",
    "c09451": "#5e3e1f",
    "c7ac65": "#554019",
    "4d4d4d": "#999999",
    "a6a6a6": "#7a7a7a"
}

def get_colors(dark_mode: bool):
    return colors_dark if dark_mode else colors
def obtener_contenido():
    temas = [
        {
            "titulo": "Energía Cinética",
            "descripcion": "Es la energía que posee un cuerpo debido a su movimiento.",
            "formula": "Ec = ½mv²",
            "ejemplo": "Una pelota de 0.5 kg que se mueve a 10 m/s tiene Ec = 25 J"
        },
        {
            "titulo": "Energía Potencial",
            "descripcion": "Es la energía que un cuerpo tiene debido a su posición o altura.",
            "formula": "Ep = mgh",
            "ejemplo": "Una roca de 2 kg a 5 m de altura tiene Ep = 98 J"
        }
    ]

    return {
        "titulo": "Módulo de Física",
        "descripcion": "Explora las leyes fundamentales del universo: energía cinética y potencial.",
        "temas": temas
    }

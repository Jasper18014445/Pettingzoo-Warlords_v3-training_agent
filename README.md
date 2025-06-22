__        __           _               _  
\ \      / / __ _ _ _ | | ___  _ _   _| | ___
 \ \ /\ / / / _` | '__| |/ _ \| '_|/ _` |/ __|
  \ V  V / | (_| | |  | | (_) | | (_|_|_|| __\
   \_/\_/   \__,_|_|  |_|\___/|_|  \__,_|_ __/

   ____  ____   ___  
  |  _ \|  _ \ / _ \ 
  | |_) | |_) | | | |
  |  __/|  __/| |_| |
  |_|   |_|    \___/ 





# Inhoudsopgave
- Korte beschrijving
- Installatie-instructies en opstart
- Hoe te starten
- Functionaliteiten 
- Bijdragen
- Licentie
- Contact / Issues melden


### Korte Beschrijving###
Het spel Warlords draait om een balletje dat rondgaat in een omgeving met vier verschillende burchten waar 
kastelen achter schuilgaan. Elke burcht heeft een agent die hem verdedigt met een schijfje waar de bal 
op kan landen en vanaf kan kaatsen.
In de onderhavige code worden agents getraind die zelf het spel kunnen spelen.


### Installatie-instructies en opstart###
Run het notebook in een Linux-omgeving, in Google Colab of in een andere omgeving die Linux aankan. 


### Functionaliteiten ###
Reinforcement learning met behulp van PPO (Proximal Policy Optimization) in een multi-agent Atari-omgeving (Warlords)

Trainingsstrategie per agent: mogelijkheid om specifieke agents afzonderlijk te trainen (specialisten) of afwisselend meerdere agents (generalist).

PPO (Proximal Policy Optimization): Algoritme dat zorgt voor een afgeknotte (clip functie) parameter update en baseert zich op toekomstige verwachte beloningen en advantage over stappen uit het verleden. 

Hyperparameteroptimalisatie via Optuna: automatische zoektocht naar de beste leerrates, gamma’s en andere instellingen.

Visuele inputverwerking via CNN en preprocessing: inclusief kleurreductie, frame stacking en resizing naar 84x84 beelden.

Gebruik van GPU-acceleratie (indien beschikbaar) voor snellere training. Let op: De gratis versie van Colab heeft gebruikslimieten op GPU-gebruik. 

Herbruikbare trainingsfases: modellen kunnen worden opgeslagen, hervat en doorgetraind zonder verlies van eerdere kennis.

Preprocessing: Een reeks wrappers past de omgeving aan: slechts één actie per vier frames, schaling pixelwaarden, kleuren, verkleining van de frames en omzetting naar de vector om ze klaar te maken voor training.


### Bijdragen###
Hyperparameter-tuning is mogelijk, evenals het doortrainen op bestaande modellen.

### Licentie###
De te gebruiken licenties om de code te kunnen runnen worden beheerd door middel van AutoROM. !AutoROM --accept-license accepteert automatisch de licentievoorwaarden van de Atari Learning Environment (ALE), zodat de ROMs legaal kunnen worden gedownload en gebruikt voor niet-commerciële trainingsdoeleinden met PettingZoo en Gymnasium.
De code zelf is eigendom van Jasper Duncker, Busse Heemskerk, Natasja de Kok en Tim Oosterling.
Dit project is opgemaakt in opdracht van Vikram Radhakrishnan ten behoeve van het vak Autonomous Systems van de Haagse Hogeschool, collegejaar 2024-2025.



### Contact / Issues melden###
Kies één van de onderstaande e-mailadressen om contact op te nemen met de ontwikkelaars of een probleem met de code te melden.
j.w.duncker@student.hhs.nl
b.j.heemskerk-1@student.hhs.nl
n.n.j.de.kok@student.hhs.nl
t.oosterling@student.hhs.nl



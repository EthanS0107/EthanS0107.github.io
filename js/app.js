const links = document.querySelectorAll("nav li");
icons.addEventListener("click", () => {
  nav.classList.toggle("active");
});

links.forEach((link) => {
  link.addEventListener("click", () => {
    nav.classListe.remove("active");
  });
});

const bouton_active_sport = document.querySelector("#bouton-active-sport");
const texte_sport = document.querySelector("#texte-sport");
const bouton_active_voyage = document.querySelector("#bouton-active-voyage");
const texte_voyage = document.querySelector("#texte-voyage");
const bouton_active_pêche = document.querySelector("#bouton-active-pêche");
const texte_pêche = document.querySelector("#texte-pêche");
const bouton_active_jeu_stratégie = document.querySelector(
  "#bouton-active-jeu-stratégie"
);
const texte_jeu_stratégie = document.querySelector("#texte-jeu-stratégie");
const bouton_active_jeu_vidéo = document.querySelector(
  "#bouton-active-jeu-vidéo"
);
const texte_jeu_vidéo = document.querySelector("#texte-jeu-vidéo");

bouton_active_sport.addEventListener("click", () => {
  if (texte_sport.style.display == "block") {
    texte_sport.style.display = "none";
    texte_sport.style.position = "absolute";
  } else {
    texte_sport.style.display = "block";
    texte_sport.style.position = "relative";
    if (texte_voyage.style.display == "block") {
      texte_voyage.style.display = "none";
      texte_voyage.style.position = "absolute";
    }
    if (texte_pêche.style.display == "block") {
      texte_pêche.style.display = "none";
      texte_pêche.style.position = "absolute";
    }
    if (texte_jeu_stratégie.style.display == "block") {
      texte_jeu_stratégie.style.display = "none";
      texte_jeu_stratégie.style.position = "absolute";
    }
    if (texte_jeu_vidéo.style.display == "block") {
      texte_jeu_vidéo.style.display = "none";
      texte_jeu_vidéo.style.position = "absolute";
    }
  }
});

bouton_active_voyage.addEventListener("click", () => {
  if (texte_voyage.style.display == "block") {
    texte_voyage.style.display = "none";
    texte_voyage.style.position = "absolute";
  } else {
    texte_voyage.style.display = "block";
    texte_voyage.style.position = "relative";
    if (texte_sport.style.display == "block") {
      texte_sport.style.display = "none";
      texte_sport.style.position = "absolute";
    }
    if (texte_pêche.style.display == "block") {
      texte_pêche.style.display = "none";
      texte_pêche.style.position = "absolute";
    }
    if (texte_jeu_stratégie.style.display == "block") {
      texte_jeu_stratégie.style.display = "none";
      texte_jeu_stratégie.style.position = "absolute";
    }
    if (texte_jeu_vidéo.style.display == "block") {
      texte_jeu_vidéo.style.display = "none";
      texte_jeu_vidéo.style.position = "absolute";
    }
  }
});

bouton_active_pêche.addEventListener("click", () => {
  if (texte_pêche.style.display == "block") {
    texte_pêche.style.display = "none";
    texte_pêche.style.position = "absolute";
  } else {
    texte_pêche.style.display = "block";
    texte_pêche.style.position = "relative";
    if (texte_voyage.style.display == "block") {
      texte_voyage.style.display = "none";
      texte_voyage.style.position = "absolute";
    }
    if (texte_sport.style.display == "block") {
      texte_sport.style.display = "none";
      texte_sport.style.position = "absolute";
    }
    if (texte_jeu_stratégie.style.display == "block") {
      texte_jeu_stratégie.style.display = "none";
      texte_jeu_stratégie.style.position = "absolute";
    }
    if (texte_jeu_vidéo.style.display == "block") {
      texte_jeu_vidéo.style.display = "none";
      texte_jeu_vidéo.style.position = "absolute";
    }
  }
});

bouton_active_jeu_stratégie.addEventListener("click", () => {
  if (texte_jeu_stratégie.style.display == "block") {
    texte_jeu_stratégie.style.display = "none";
    texte_jeu_stratégie.style.position = "absolute";
  } else {
    texte_jeu_stratégie.style.display = "block";
    texte_jeu_stratégie.style.position = "relative";
    if (texte_voyage.style.display == "block") {
      texte_voyage.style.display = "none";
      texte_voyage.style.position = "absolute";
    }
    if (texte_pêche.style.display == "block") {
      texte_pêche.style.display = "none";
      texte_pêche.style.position = "absolute";
    }
    if (texte_sport.style.display == "block") {
      texte_sport.style.display = "none";
      texte_sport.style.position = "absolute";
    }
    if (texte_jeu_vidéo.style.display == "block") {
      texte_jeu_vidéo.style.display = "none";
      texte_jeu_vidéo.style.position = "absolute";
    }
  }
});

bouton_active_jeu_vidéo.addEventListener("click", () => {
  if (texte_jeu_vidéo.style.display == "block") {
    texte_jeu_vidéo.style.display = "none";
    texte_jeu_vidéo.style.position = "absolute";
  } else {
    texte_jeu_vidéo.style.display = "block";
    texte_jeu_vidéo.style.position = "relative";
    if (texte_voyage.style.display == "block") {
      texte_voyage.style.display = "none";
      texte_voyage.style.position = "absolute";
    }
    if (texte_pêche.style.display == "block") {
      texte_pêche.style.display = "none";
      texte_pêche.style.position = "absolute";
    }
    if (texte_jeu_stratégie.style.display == "block") {
      texte_jeu_stratégie.style.display = "none";
      texte_jeu_stratégie.style.position = "absolute";
    }
    if (texte_sport.style.display == "block") {
      texte_sport.style.display = "none";
      texte_sport.style.position = "absolute";
    }
  }
});

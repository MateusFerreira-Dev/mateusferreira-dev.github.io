/* RESET */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* BODY + FUNDO MODERNO */
body {
  font-family: Arial, sans-serif;
  background: linear-gradient(135deg, #020617, #0f172a, #1e293b);
  color: #e2e8f0;
  min-height: 100vh;
  animation: fadeIn 0.8s ease-in;
  position: relative;
}

/* EFEITO DE LUZ NO FUNDO */
body::before {
  content: "";
  position: fixed;
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(56,189,248,0.15), transparent);
  top: -100px;
  left: -100px;
  z-index: -1;
}

body::after {
  content: "";
  position: fixed;
  width: 500px;
  height: 500px;
  background: radial-gradient(circle, rgba(99,102,241,0.15), transparent);
  bottom: -100px;
  right: -100px;
  z-index: -1;
}

/* HEADER */
header {
  text-align: center;
  padding: 100px 20px;
}

header h1 {
  font-size: 3rem;
  margin-bottom: 10px;
}

header p {
  color: #94a3b8;
  font-size: 1.2rem;
}

/* SECTIONS */
section {
  max-width: 1000px;
  margin: auto;
  padding: 40px 20px;
}

/* GLASS CARD BASE */
.glass {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(12px);
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

/* TITULOS */
h2 {
  color: #38bdf8;
  margin-bottom: 20px;
}

/* GRID */
.projetos {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
}

/* CARD */
.card {
  padding: 20px;
  transition: 0.3s;
}

.card:hover {
  transform: translateY(-8px) scale(1.01);
  border: 1px solid rgba(56,189,248,0.4);
}

/* TECNOLOGIAS */
.tech {
  margin-top: 12px;
}

.tech span {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(15, 23, 42, 0.6);
  padding: 5px 10px;
  margin-right: 6px;
  border-radius: 6px;
  font-size: 12px;
  border: 1px solid rgba(255,255,255,0.1);
}

.tech i {
  font-size: 14px;
}

/* LINKS */
.links {
  margin-top: 15px;
}

.links a {
  text-decoration: none;
  color: #38bdf8;
  font-weight: bold;
}

/* CONTATO */
section a {
  display: inline-block;
  margin-right: 15px;
  margin-top: 10px;
  color: #38bdf8;
  text-decoration: none;
  font-weight: bold;
}

/* HOVER GLOBAL */
a {
  transition: all 0.2s ease;
}

a:hover {
  color: #7dd3fc;
  transform: translateY(-2px);
}

/* FOOTER */
footer {
  text-align: center;
  padding: 20px;
  color: #94a3b8;
}

/* ANIMAÇÃO */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(15px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

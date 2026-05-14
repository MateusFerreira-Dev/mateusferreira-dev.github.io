document.addEventListener("DOMContentLoaded", () => {
  const eyes = document.querySelectorAll(".eye");
  const mascot = document.querySelector(".mascot");

  let mouseX = 0;
  let mouseY = 0;

  let currentX = 100;
  let currentY = 75;

  document.addEventListener("mousemove", (e) => {
    mouseX = Math.max(
      -10,
      Math.min(10, (e.clientX / window.innerWidth - 0.5) * 20),
    );
    mouseY = Math.max(
      -10,
      Math.min(10, (e.clientY / window.innerHeight - 0.5) * 20),
    );

    const moveX = (e.clientX / window.innerWidth - 0.5) * 6;
    const moveY = (e.clientY / window.innerHeight - 0.5) * 6;

    const hero = document.querySelector(".hero");
    if (hero) {
      hero.style.transform = `translate(${moveX}px, ${moveY}px)`;
    }
  });

  function animateEye() {
    currentX += (100 + mouseX - currentX) * 0.08;
    currentY += (75 + mouseY - currentY) * 0.08;

    eyes.forEach((eye, index) => {
      const offset = index === 0 ? -20 : 20;
      eye.setAttribute("cx", currentX + offset);
      eye.setAttribute("cy", currentY);
    });

    requestAnimationFrame(animateEye);
  }

  animateEye();

  function blink() {
    eyes.forEach((eye) => {
      eye.style.transform = "scaleY(0.1)";
    });

    setTimeout(() => {
      eyes.forEach((eye) => {
        eye.style.transform = "scaleY(1)";
      });
    }, 120);

    const nextBlink = 2000 + Math.random() * 3000;
    setTimeout(blink, nextBlink);
  }

  blink();

  mascot.addEventListener("mouseenter", () => {
    eyes.forEach((eye) => eye.setAttribute("r", 7));
  });

  mascot.addEventListener("mouseleave", () => {
    eyes.forEach((eye) => eye.setAttribute("r", 6));
  });
});

// ===== PARTICULAS PRO =====

const canvas = document.getElementById("particles");

if (canvas) {
  const ctx = canvas.getContext("2d");

  let particles = [];
  const PARTICLE_COUNT = window.innerWidth < 768 ? 40 : 70;

  let mouse = {
    x: null,
    y: null,
  };

  window.addEventListener("mousemove", (e) => {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
  });

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }

  resize();

  function initParticles() {
    particles = [];
    for (let i = 0; i < PARTICLE_COUNT; i++) {
      particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        r: Math.random() * 2,
        dx: (Math.random() - 0.5) * 0.3,
        dy: (Math.random() - 0.5) * 0.3,
      });
    }
  }

  initParticles();

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // 🌌 desenhar partículas
    particles.forEach((p) => {
      // 🧲 campo magnético (atração leve)
      if (mouse.x && mouse.y) {
        let dx = mouse.x - p.x;
        let dy = mouse.y - p.y;
        let dist = dx * dx + dy * dy;

        if (dist < 20000) {
          p.x += dx * 0.0005;
          p.y += dy * 0.0005;
        }
      }

      p.x += p.dx;
      p.y += p.dy;

      if (p.x < 0 || p.x > canvas.width) p.dx *= -1;
      if (p.y < 0 || p.y > canvas.height) p.dy *= -1;

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = "#38bdf8";
      ctx.fill();
    });

    // 🔗 conexões entre partículas
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        let dx = particles[i].x - particles[j].x;
        let dy = particles[i].y - particles[j].y;
        let dist = dx * dx + dy * dy;

        if (dist < 12000) {
          let opacity = 1 - dist / 12000;

          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);

          ctx.strokeStyle = `rgba(56,189,248,${opacity})`;
          ctx.lineWidth = 0.5;

          ctx.shadowBlur = 10; // ✨ glow
          ctx.shadowColor = "#38bdf8";

          ctx.stroke();

          ctx.shadowBlur = 0; // reset
        }
      }
    }

    // 🧠 conexão com mouse
    particles.forEach((p) => {
      if (mouse.x && mouse.y) {
        let dx = p.x - mouse.x;
        let dy = p.y - mouse.y;
        let dist = dx * dx + dy * dy;

        if (dist < 15000) {
          let opacity = 1 - dist / 15000;

          ctx.beginPath();
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(mouse.x, mouse.y);

          ctx.strokeStyle = `rgba(56,189,248,${opacity})`;
          ctx.lineWidth = 1;

          ctx.shadowBlur = 15; // glow mais forte
          ctx.shadowColor = "#38bdf8";

          ctx.stroke();

          ctx.shadowBlur = 0;
        }
      }
    });

    requestAnimationFrame(draw);
  }

  draw();

  window.addEventListener("resize", () => {
    resize();
    initParticles();
  });
}

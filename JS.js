document.addEventListener("DOMContentLoaded", () => {
  const eye = document.getElementById("eye");
  const mascot = document.querySelector(".mascot");

  let mouseX = 0;
  let mouseY = 0;

  let currentX = 100;
  let currentY = 100;

  // 👀 seguir mouse suave
  document.addEventListener("mousemove", (e) => {
    mouseX = (e.clientX / window.innerWidth - 0.5) * 20;
    mouseY = (e.clientY / window.innerHeight - 0.5) * 20;

    // parallax
    const moveX = (e.clientX / window.innerWidth - 0.5) * 10;
    const moveY = (e.clientY / window.innerHeight - 0.5) * 10;
    document.body.style.transform = `translate(${moveX}px, ${moveY}px)`;
  });

  function animateEye() {
    currentX += (100 + mouseX - currentX) * 0.1;
    currentY += (100 + mouseY - currentY) * 0.1;

    eye.setAttribute("cx", currentX);
    eye.setAttribute("cy", currentY);

    requestAnimationFrame(animateEye);
  }

  animateEye();

  // 😉 piscar (FUNCIONA DE VERDADE AGORA)
  setInterval(() => {
    eye.style.transform = "scaleY(0.2)";
    setTimeout(() => {
      eye.style.transform = "scaleY(1)";
    }, 120);
  }, 2500);

  // ⚡ hover
  mascot.addEventListener("mouseenter", () => {
    eye.setAttribute("r", 24);
  });

  mascot.addEventListener("mouseleave", () => {
    eye.setAttribute("r", 20);
  });
});

// ===== PARTICULAS =====

const canvas = document.getElementById("particles");

if (canvas) {
  const ctx = canvas.getContext("2d");

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }

  resize();

  let particles = [];

  for (let i = 0; i < 70; i++) {
    particles.push({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      r: Math.random() * 2,
      dx: (Math.random() - 0.5) * 0.4,
      dy: (Math.random() - 0.5) * 0.4,
    });
  }

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    particles.forEach((p) => {
      p.x += p.dx;
      p.y += p.dy;

      if (p.x < 0 || p.x > canvas.width) p.dx *= -1;
      if (p.y < 0 || p.y > canvas.height) p.dy *= -1;

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = "#38bdf8";
      ctx.fill();
    });

    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        let dx = particles[i].x - particles[j].x;
        let dy = particles[i].y - particles[j].y;
        let dist = dx * dx + dy * dy;

        if (dist < 14000) {
          let opacity = 1 - dist / 14000;

          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.strokeStyle = `rgba(56,189,248,${opacity})`;
          ctx.lineWidth = 0.5;
          ctx.stroke();
        }
      }
    }

    requestAnimationFrame(draw);
  }

  draw();

  window.addEventListener("resize", resize);
}

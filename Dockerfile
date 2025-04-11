FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y \
    nasm \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY solution.asm .

CMD ["sh", "-c", "nasm -f elf64 solution.asm && gcc -no-pie -o solution solution.o && ./solution"]
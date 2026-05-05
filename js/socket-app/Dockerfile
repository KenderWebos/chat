# Etapa de construcción
FROM node:18-alpine AS builder

WORKDIR /app

# Copiar package.json y package-lock.json
COPY package*.json ./

# Instalar dependencias
RUN npm ci

# Etapa de producción
FROM node:18-alpine

WORKDIR /app

# Instalar curl para healthcheck
RUN apk add --no-cache curl

# Copiar node_modules del builder
COPY --from=builder /app/node_modules ./node_modules

# Copiar el código de la aplicación
COPY . .

# Exponer el puerto
EXPOSE 8000

# Variables de entorno por defecto
ENV NODE_ENV=production
ENV PORT=8000

# Comando para iniciar la aplicación
CMD ["npm", "start"]

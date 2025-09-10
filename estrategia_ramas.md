# Estrategia de Ramificación - Proyecto ROE DuPont

## Diagrama de Ramas

```
main
├── develop
│   ├── feature/configuracion-proyecto
│   ├── feature/ratios-basicos
│   ├── feature/visualizacion-3d
│   ├── feature/estados-financieros
│   └── feature/integracion-streamlit
└── hotfix/* (para correcciones urgentes)
```

## Flujo de Desarrollo Recomendado

### Fase 1: Configuración Inicial
1. Crear rama `feature/configuracion-proyecto` desde `main`
2. Configurar estructura del proyecto, dependencias y documentación
3. Mergear a `develop` y luego a `main`

### Fase 2: Desarrollo de Funcionalidades (Sprints)
Para cada funcionalidad:
1. Crear rama `feature/[nombre-funcionalidad]` desde `develop`
2. Desarrollar la funcionalidad completa
3. Mergear a `develop` para integración
4. Probar integración en `develop`
5. Mergear a `main` cuando esté estable

### Fase 3: Integración Final
1. Crear rama `feature/integracion-streamlit` desde `develop`
2. Integrar todas las funcionalidades en la aplicación principal
3. Configurar navegación y layout
4. Mergear a `develop` y luego a `main`

## Comandos Git Sugeridos

### Crear y trabajar en ramas
```bash
# Crear y cambiar a nueva rama
git checkout -b feature/ratios-basicos develop

# Trabajar en la funcionalidad
# ... commits ...

# Push de la rama
git push origin feature/ratios-basicos
```

### Merge a develop
```bash
# Cambiar a develop
git checkout develop

# Mergear la funcionalidad
git merge feature/ratios-basicos

# Push de develop
git push origin develop
```

### Merge a main
```bash
# Cambiar a main
git checkout main

# Mergear desde develop
git merge develop

# Push de main
git push origin main
```

## Beneficios de esta Estrategia

1. **Desarrollo Paralelo**: Cada funcionalidad se puede desarrollar independientemente
2. **Integración Controlada**: `develop` permite probar integraciones antes de `main`
3. **Rollback Fácil**: Si una funcionalidad causa problemas, se puede revertir fácilmente
4. **Trazabilidad**: Cada funcionalidad tiene su historial de commits independiente
5. **Colaboración**: Múltiples desarrolladores pueden trabajar en diferentes funcionalidades simultáneamente

# Examen_parcial_Poo![diagram](https://github.com/user-attachments/assets/b01ca3f6-c690-4058-97ab-d49c158b2b57)
graph TD
    %% Program Flow
    subgraph "Program Flow"
        A["Main Entry (main.py)"]:::module
        B["Controller/Launcher (Lanzador.py)"]:::module
        A -->|"calls"| B
    end

    %% Domain Models
    subgraph "Domain Models"
        C(("Point Class (Clase_punto.py)")):::domain
        D(("Rectangle Class (Rectangulos_clase.py)")):::domain
        B -->|"instantiates"| C
        B -->|"instantiates"| D
        D -->|"uses"| C
    end

    %% Legend
    Legend["Legend: Rectangle = Module, Ellipse = Domain Model"]:::legend

    %% Click Events
    click A "https://github.com/aneprados/examen_parcial_poo/blob/main/main.py"
    click B "https://github.com/aneprados/examen_parcial_poo/blob/main/Lanzador.py"
    click C "https://github.com/aneprados/examen_parcial_poo/blob/main/Clase_punto.py"
    click D "https://github.com/aneprados/examen_parcial_poo/blob/main/Rectangulos_clase.py"

    %% Styles
    classDef module fill:#cce5ff,stroke:#0056b3,stroke-width:2px;
    classDef domain fill:#d4edda,stroke:#155724,stroke-width:2px;
    classDef legend fill:#fff3cd,stroke:#856404,stroke-width:2px,dasharray: 5 5;


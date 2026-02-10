```mermaid
classDiagram
class PresentationLayer {
    <<Interface>>
    +API/Endpoints
    +Controllers
}
class BusinessLogicLayer {
    +HBnBFacade
    +Models
    +Services
}
class PersistenceLayer {
    +Repositories
    +Database
}
PresentationLayer --> BusinessLogicLayer : Facade Pattern
BusinessLogicLayer --> PersistenceLayer : Database Operations
```

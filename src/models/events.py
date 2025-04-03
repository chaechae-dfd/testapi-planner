from pydantic import BaseModel, ConfigDict

class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str 
    tags: list[str]
    location: str 
    created_at: str 
    
    model_config= ConfigDict(
        json_schema_extra={
            "example":{
                "id":1,
                "title":"아...집가고싶다",
                "image":"path/to",
                "description": "마라탕",
                "tags": ['#귀차니즘',"강의"],
                "location":"제1실습관 207호"
            }
            }) #계약된 클래스 변경불가
    
    
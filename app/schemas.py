from pydantic import BaseModel

# input schema
class PumpData(BaseModel):
     amount_tsh: float
     gps_height: int
     population: int
     age: float
     month_recorded: int
     permit: bool   
     waterpoint_type_group: str    
     source_class: str    
     quantity: str    
     quality_group: str    
     payment_type: str    
     management_group: str    
     extraction_type_class: str    
     region: str    
     basin: str   


#Request structure from client
#Defines
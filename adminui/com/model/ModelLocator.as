package com.model
{
  import mx.controls.Alert;
  import mx.rpc.events.FaultEvent;
  
  [Bindable]
  public class ModelLocator {
    private static var modelLocator:ModelLocator;

    public var base_url:String = 'http://localhost:5000';
    
    public static function getInstance() : ModelLocator {
      if (modelLocator == null)
        modelLocator = new ModelLocator();
      return modelLocator;
    }
    
    public function serviceFault(event:FaultEvent) : void {
      Alert.show("Could not contact the server, please try again later.", "Error");
    }
    
    public function ModelLocator()  {
      
    }
    
  }
  
}
from Tkinter import*
import Tkinter

class MouseLocation( Frame ):
   def __init__( self ):
      Frame.__init__( self )
      self.pack( expand = YES, fill = BOTH )
      self.master.title( "Mouse Events" )
      self.master.geometry(  "400x300" )
      self.mousePosition = StringVar() # displays mouse position
      self.mousePosition.set( "Mouse outside window" )
      self.positionLabel = Label( self,textvariable = self.mousePosition )
      self.positionLabel.pack( side = BOTTOM )
      self.bind( "<Button-1>", self.buttonPressed )
      self.bind( "<ButtonRelease-1>", self.buttonReleased )   
      self.bind( "<Enter>", self.enteredWindow )
      self.bind( "<Leave>", self.exitedWindow )
      self.bind( "<B1-Motion>", self.mouseDragged )

   def buttonPressed( self, event ):
      self.mousePosition.set( "Pressed at [ " + str( event.x ) + ", " + str( event.y ) + " ]" )

   def buttonReleased( self, event ):
      self.mousePosition.set( "Released at [ " + str( event.x ) + ", " + str( event.y ) + " ]" )

   def enteredWindow( self, event ):
      self.mousePosition.set( "Mouse in window" )

   def exitedWindow( self, event ):
      self.mousePosition.set( "Mouse outside window" )

   def mouseDragged( self, event ):
      self.mousePosition.set( "Dragged at [ " + str( event.x ) + ", " + str( event.y ) + " ]" )

MouseLocation().mainloop()

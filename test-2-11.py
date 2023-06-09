from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from core.uniform import Uniform
from OpenGL.GL import *

class Test(Base):
    def initialize(self):
        print("Initializing program...")
        ### initialize program ###
        vsCode = """
         in vec3 position;
         uniform vec3 translation;
         void main()
         {
            vec3 pos = position + translation;
            gl_Position = vec4(pos.x, pos.y, pos.z,1.0);
         }
         """
        fsCode = """
         uniform vec3 baseColor;
         out vec4 fragColor;
         void main()
         {
            fragColor = vec4(baseColor.r, baseColor.g, baseColor.b,1.0);
         }
         """
        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)
        glClearColor(0.0, 0.0, 0.0, 1.0)
          ### set up vertex array object ###
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)
        ### set up vertex attribute ###
        positionData = [ [0.0, 0.2, 0.0], [0.2, -0.2,0.0],[-0.2, -0.2, 0.0] ]
        self.vertexCount = len(positionData)
        positionAttribute = Attribute("vec3",positionData)
        positionAttribute.associateVariable(self.programRef, "position" )
          ### set up uniforms ###
        self.translation = Uniform("vec3", [-0.5, 0.0,0.0])
        self.translation.locateVariable(self.programRef, "translation" )
        self.baseColor = Uniform("vec3", [1.0, 0.0,0.0])
        self.baseColor.locateVariable( self.programRef, "baseColor" )
        #nuevo codigo
        self.speed = 0.5
    def update(self):
        #Dentro del método, calcula la distancia que debe moverse el objeto en función de su velocidad
        # y el tiempo transcurrido desde el último cuadro deltaTime.
        distance = self.speed * self.deltaTime
        #si se han pulsado las teclas "izquierda", "derecha", "abajo" o "arriba" desde el último fotograma
        # mediante el método isKeyPressed del objeto de entrada.
        if self.input.isKeyPressed("left"):
            self.translation.data[0] -= distance
        if self.input.isKeyPressed("right"):
            self.translation.data[0] += distance
        if self.input.isKeyPressed("down"):
            self.translation.data[1] -= distance
        if self.input.isKeyPressed("up"):
            self.translation.data[1] += distance
            #self.translation.data[0] += 0.01
        #if self.translation.data[0] > 1.2:
         #   self.translation.data[0] = -1.2
        #glClear(GL_COLOR_BUFFER_BIT)
        #glUseProgram( self.programRef )
        #self.translation.uploadData()
        #self.baseColor.uploadData()
        #glDrawArrays( GL_TRIANGLES , 0 , self.vertexCount)
Test().run()
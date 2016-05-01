Game = function(game){}

Game.prototype ={
    create:function(){
        this.GRAVITY = 200;
        this.background = 
                this.game.add.tileSprite(0,0,
                this.game.width,this.game.height,
                'background');
        this.background.autoScroll(-200,0);
    var style ={
        fontSize:"25px",
        fill:"#FFF"
    };
        this.text=this.game.add.text(0,0,'Clicl to start',style);
        
        this.text.anchor.setTo(0.5);
        
        this.text.x=this.game.world.centerX;
        this.text.y=this.game.world.centerY;
        
        this.text.inputEnabled=true;
        this.text.events.onInputDown.add(this.connect,this);
        this.player = this.game.add.sprite(0,0,'player');
        this.game.physics.startSystem(Phaser.Physics.ARCADE);
        this.game.physics.arcade.gravity.y = this.GRAVITY;
        
        this.game.physics.arcade.enable(this.player);
        //this.player.body.immovable = true;
        this.game.input.onDown.add(this.flap,this);
        this.elapsed = 0;
        this.gameOver = false;
        this.walls = this.game.add.group();
    },
    connect:function(){
       this.callFBSDK();  
    },
    //Agrega la conexion a Fb 
    callFBSDK:function(){
      FB.login(function(response){
          if(response.status=='connected'){
              FB.api("/me",function(response){//tarea que te jale la foto de perfil solo el url 
                 console.log(response); 
              });
          }
      },{scope:'public_profile'}); 
    },
    flap:function(){
        this.player.body.velocity.y = -200;
    },
    update:function(){
        if(!this.gameOver){
            this.elapsed+= this.game.time.elapsed;
            if(this.elapsed>=3000){
                this.elapsed = 0;
                this.spawnWalls();
            }
            
            this.game.physics.arcade.collide(
                this.player,this.walls
                ,function(player,wall){
                    if(!this.gameOver){
                        this.gameOver = true;
                        console.log("moristes");
                    }
                    
                },null,this);
        }
    },
    spawnWalls: function(){
        var wallY = this.rnd.integerInRange
            (this.game.height *.3, this.game.height *.7);
        var botWall = this.generateWall(wallY);
        var topWall = this.generateWall(wallY, true);
    },
    
    generateWall:function(wallY,flipped){
        var posY ;
        var opening  = 100;
        if(flipped){
            wallY = wallY - (opening/2);
        }else{
            wallY = wallY + (opening/2);
        }
        var wall = this.game.add.sprite(this.game.width,
                wallY,'wall');
        this.game.physics.arcade.enable(wall);
        wall.body.velocity.x = -200;
        if(flipped){
            wall.scale.y = -1;
            wall.body.offset.y  = -wall.body.height;
        }
        wall.body.immovable = true;
        wall.body.allowGravity = false;
        this.walls.add(wall);
    }
    
    
    
    
    
    
    
    
    
}
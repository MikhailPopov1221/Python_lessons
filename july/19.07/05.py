



def take_damage(self, damage):
    real_damage = damage - self.armor
    if real_damage < 0:
        real_damage = 0
    super().take_damage(real_damage)
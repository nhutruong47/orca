# Knowledge Document: DebugController.java (Chunk 8/8)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/DebugController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "admin",
  "tags": [
    "admin",
    "security",
    "factory",
    "inventory",
    "employee"
  ],
  "logical_type": "Controller",
  "chunk_index": 7,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, security, factory, inventory, employee

## Source Code Chunk
```java
        u.setEmail("trangdh857@demo.com");
            u.setRole(Role.MEMBER);
            return u;
        });
        owner.setPassword(passwordEncoder.encode("123456"));
        final User finalOwner = userRepository.save(owner);

        // Create team
        Team team = teamRepository.findAll().stream().filter(t -> "Nhà máy Đặng Hải Trang".equals(t.getName())).findFirst().orElseGet(() -> {
            Team t = new Team();
            t.setName("Nhà máy Đặng Hải Trang");
            t.setDescription("Nhà máy cà phê quy mô 20 thành viên.");
            t.setOwner(finalOwner);
            return teamRepository.save(t);
        });

        // Create 20 members
        for (int i = 1; i <= 20; i++) {
            final int index = i;
            User memberUser = userRepository.findByUsername("member_demo_" + i).orElseGet(() -> {
                User u = new User();
                u.setUsername("member_demo_" + index);
                u.setPassword(passwordEncoder.encode("123456"));
                u.setFullName("Thành viên " + index);
                u.setEmail("member" + index + "@demo.com");
                u.setRole(Role.MEMBER);
                return userRepository.save(u);
            });

            // Check if team member exists
            long count = (long) entityManager.createQuery("SELECT COUNT(tm) FROM TeamMember tm WHERE tm.team = :team AND tm.user = :user")
                    .setParameter("team", team)
                    .setParameter("user", memberUser)
                    .getSingleResult();
            if (count == 0) {
                TeamMember tm = new TeamMember();
                tm.setTeam(team);
                tm.setUser(memberUser);
                tm.setGroupRole(GroupRole.MEMBER);
                entityManager.persist(tm);
            }
        }
        
        teamRepository.save(team);

        return Map.of("message", "Đã tạo thành công xưởng Nhà máy Đặng Hải Trang với 20 thành viên!", "owner_username", "trangdh857", "owner_password", "123456");
    }
}

```
